from pathlib import Path

from gendiff import generate_diff

ASSETS = Path(__file__).resolve().parent.parent / "tests" / "test_data"

EXPECTED = """\
{
..  common: {
......+ follow: false
......  setting1: Value 1
......- setting2: 200
......- setting3: true
......+ setting3: null
......+ setting4: blah blah
......+ setting5: {
............key5: value5
........}
......  setting6: {
..........  doge: {
..............- wow: 
..............+ wow: so much
............}
..........  key: value
..........+ ops: vops
........}
....}
..  group1: {
......- baz: bas
......+ baz: bars
......  foo: bar
......- nest: {
............key: value
........}
......+ nest: str
....}
..- group2: {
........abc: 12345
........deep: {
............id: 45
........}
....}
..+ group3: {
........deep: {
............id: {
................number: 45
............}
........}
........fee: 100500
....}
}"""


def draw_dots(text: str) -> str:
    return text.replace(" ", ".")


def test_generate_diff():
    file_path1 = ASSETS / "file1.json"
    file_path2 = ASSETS / "file2.json"

    result = generate_diff(file_path1, file_path2)
    assert draw_dots(result) == draw_dots(EXPECTED)


def test_generate_diff_yml():
    file_path1 = ASSETS / "file1.yml"
    file_path2 = ASSETS / "file2.yml"

    result = generate_diff(file_path1, file_path2)
    assert draw_dots(result) == draw_dots(EXPECTED)
