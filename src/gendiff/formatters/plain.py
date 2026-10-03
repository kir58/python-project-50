from __future__ import annotations

from typing import Any

from gendiff.utils import AstItem


def format_plain_value(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def walk(ast: list[AstItem], parent: str) -> list[str]:
    lines: list[str] = []

    for el in ast:
        key = el["key"]
        path = f"{parent}.{key}" if parent else key
        match el["type"]:
            case "nested":
                lines.extend(walk(el["children"], path))
            case "unchanged":
                continue
            case "added":
                value = format_plain_value(el["value"])
                lines.append(
                    f"Property '{path}' was added with value: {value}"
                )
            case "deleted":
                lines.append(f"Property '{path}' was removed")
            case "changed":
                deleted = format_plain_value(el["deleted_value"])
                added = format_plain_value(el["added_value"])
                lines.append(
                    f"Property '{path}' was updated. From {deleted} to {added}"
                )

    return lines


def format_plain(ast: list[AstItem]) -> str:
    return "\n".join(walk(ast, ""))
