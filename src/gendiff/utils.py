from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict, cast

ItemType = Literal["unchanged", "deleted", "added", "changed", "nested"]


class AstItem(TypedDict):
    type: ItemType
    key: str
    value: NotRequired[Any]
    deleted_value: NotRequired[Any]
    added_value: NotRequired[Any]
    children: NotRequired[list[AstItem]]


def make_item(item_type: ItemType, key: str, **fields: Any) -> AstItem:
    item = {"type": item_type, "key": key, **fields}
    return cast(AstItem, cast(object, item))


def build_ast(
    file_1: dict[str, Any | dict],
    file_2: dict[str, Any | dict],
) -> list[AstItem]:
    ast: list[AstItem] = []

    keys = sorted(file_1.keys() | file_2.keys())

    for key in keys:
        value_1 = file_1.get(key, None)
        value_2 = file_2.get(key, None)

        if isinstance(value_1, dict) and isinstance(value_2, dict):
            children = build_ast(value_1, value_2)
            ast.append(make_item("nested", key, children=children))
            continue
        if value_1 == value_2:
            ast.append(make_item("unchanged", key, value=value_1))
            continue

        if key in file_1.keys() and key not in file_2.keys():
            ast.append(make_item("deleted", key, value=value_1))
            continue

        if key not in file_1.keys() and key in file_2.keys():
            ast.append(make_item("added", key, value=value_2))
            continue

        ast.append(
            make_item(
                "changed",
                key,
                deleted_value=value_1,
                added_value=value_2,
            )
        )

    return ast
