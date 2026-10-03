from __future__ import annotations

from typing import Any

from gendiff.utils import AstItem


def format_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def stringify(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        closing_indent = " " * ((depth - 1) * 4)
        lines = [
            f"{indent}{key}: {stringify(inner, depth + 1)}"
            for key, inner in value.items()
        ]
        return "{{\n{}\n{}}}".format("\n".join(lines), closing_indent)

    return format_value(value)


def format_stylish(ast: list[AstItem], depth: int = 1) -> str:
    indent = " " * (depth * 4 - 2)
    closing_indent = " " * ((depth - 1) * 4)
    lines: list[str] = []

    for el in ast:
        key = el["key"]
        match el["type"]:
            case "unchanged":
                value = stringify(el["value"], depth + 1)
                lines.append(f"{indent}  {key}: {value}")
            case "changed":
                deleted = stringify(el["deleted_value"], depth + 1)
                added = stringify(el["added_value"], depth + 1)
                lines.append(f"{indent}- {key}: {deleted}")
                lines.append(f"{indent}+ {key}: {added}")
            case "added":
                value = stringify(el["value"], depth + 1)
                lines.append(f"{indent}+ {key}: {value}")
            case "deleted":
                value = stringify(el["value"], depth + 1)
                lines.append(f"{indent}- {key}: {value}")
            case "nested":
                children = format_stylish(el["children"], depth + 1)
                lines.append(f"{indent}  {key}: {children}")

    return "{{\n{}\n{}}}".format("\n".join(lines), closing_indent)
