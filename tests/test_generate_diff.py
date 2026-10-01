from pathlib import Path

from gendiff import generate_diff

ASSETS = Path(__file__).resolve().parent.parent / "assets"

EXPECTED = """\
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff():
    file_path1 = ASSETS / "file1.json"
    file_path2 = ASSETS / "file2.json"

    assert generate_diff(file_path1, file_path2) == EXPECTED
