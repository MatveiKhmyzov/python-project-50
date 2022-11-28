#! usr/bin/env python3

from gendiff import generate_diff
from gendiff import get_args


def main():
    path1, path2, format_name = get_args()
    print(generate_diff(path1, path2, format_name))


if __name__ == '_main_':
    main()
