#! usr/bin/env python3

from gendiff import generate_diff, reader
from gendiff import get_formatted_data
from gendiff import get_args


def main():
    formatter, path1, path2 = get_args()
    file1, file2 = reader(path1, path2)
    print(get_formatted_data(generate_diff(file1, file2), formatter))


if __name__ == '_main_':
    main()
