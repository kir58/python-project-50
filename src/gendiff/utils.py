from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict, cast


ItemType = Literal["unchanged", "deleted", "added", "changed"]


class AstItem(TypedDict):
    type: ItemType
    key: str
    value: NotRequired[Any]
    deleted_value: NotRequired[Any]
    added_value: NotRequired[Any]


def make_item(item_type: ItemType, key: str, **fields: Any) -> AstItem:
    return cast(AstItem, cast(object, {"type": item_type, "key": key, **fields}))


def build_ast(file_1: dict[str, Any], file_2: dict[str, Any]) -> list[AstItem]:
    ast: list[AstItem] = []

    keys = sorted(file_1.keys() | file_2.keys())

    for key in keys:
        value_1 = file_1.get(key, None)
        value_2 = file_2.get(key, None)

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


def format_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def render(ast: list[AstItem]) -> str:
    result: list[str] = []
    for el in ast:
        match el["type"]:
            case "unchanged":
                result.append(f"    {el['key']}: {format_value(el['value'])}")
            case "changed":
                result.append(
                    f"  - {el['key']}: {format_value(el['deleted_value'])}"
                )
                result.append(
                    f"  + {el['key']}: {format_value(el['added_value'])}"
                )
            case "added":
                result.append(f"  + {el['key']}: {format_value(el['value'])}")
            case "deleted":
                result.append(f"  - {el['key']}: {format_value(el['value'])}")

    return "{{\n{}\n}}".format("\n".join(result))
