from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json


def get_formatted_data(file, name_format):
    if name_format == "stylish":
        return get_stylish(file)
    if name_format == "plain":
        return get_plain(file)
    if name_format == "json":
        return get_json(file)
    else:
        print("Unknown format!")
        return get_stylish(file)
