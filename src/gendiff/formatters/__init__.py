from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff, format_name):
    match format_name:
        case "stylish":
            return format_stylish(diff)
        case "plain":
            return format_plain(diff)
        case "json":
            return format_json(diff)
        case _:
            raise ValueError(f"Unknown format: {format_name}")
