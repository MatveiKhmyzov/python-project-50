from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain


def get_formatted_data(file, name_format):
    if name_format == "stylish":
        return get_stylish(file)
    if name_format == "plain":
        return get_plain(file)
    else:
        print("Unknown format!")
        return get_stylish(file)
