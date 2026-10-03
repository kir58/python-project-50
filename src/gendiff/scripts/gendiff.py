import argparse
import json

from gendiff.utils import build_ast, render


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def generate_diff(file_path_1, file_path_2):
    data1 = read_json(file_path_1)
    data2 = read_json(file_path_2)

    return render(build_ast(data1, data2))


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
