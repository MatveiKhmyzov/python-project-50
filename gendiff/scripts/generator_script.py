#! usr/bin/env python3

from gendiff.parser import generate_diff
from gendiff.cli import get_args


def main():
    path1, path2 = get_args()
    print(generate_diff(path1, path2))


if __name__ == '_main_':
    main()
