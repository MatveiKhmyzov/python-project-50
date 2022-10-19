#! usr/bin/env python3

from gendiff.generator import generate_diff, generate_reference


def main():
    path1, path2 = generate_reference()
    print(generate_diff(path1, path2))


if __name__ == '_main_':
    main()
