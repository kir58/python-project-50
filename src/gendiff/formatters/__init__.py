from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format_diff(diff, format_name):
    match format_name:
        case "stylish":
            return format_stylish(diff)
        case "plain":
            return format_plain(diff)
        case _:
            raise ValueError(f"Unknown format: {format_name}")
