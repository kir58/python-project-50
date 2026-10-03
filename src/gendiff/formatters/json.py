import json

from gendiff.utils import AstItem


def format_json(ast: list[AstItem]) -> str:
    return json.dumps(ast)
