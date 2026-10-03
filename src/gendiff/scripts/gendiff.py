import argparse

from gendiff.formatters import format_diff
from gendiff.read_file import read_file
from gendiff.utils import build_ast


def generate_diff(file_path_1, file_path_2, format_name="stylish"):
    data1 = read_file(file_path_1)
    data2 = read_file(file_path_2)

    return format_diff(build_ast(data1, data2), format_name)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help="set format of output",
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
