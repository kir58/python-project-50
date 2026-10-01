import argparse
import json


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


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

    data1 = read_json(args.first_file)
    data2 = read_json(args.second_file)
    print(data1)
    print(data2)


if __name__ == "__main__":
    main()
