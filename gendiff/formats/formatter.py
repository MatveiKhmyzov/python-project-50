from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json


STYLISH_FORMAT = 'stylish'
PLAIN_FORMAT = 'plain'
JSON_FORMAT = "json"


def get_formatted_data(file, name_format):
    if name_format == STYLISH_FORMAT:
        return get_stylish(file)
    if name_format == PLAIN_FORMAT:
        return get_plain(file)
    if name_format == JSON_FORMAT:
        return get_json(file)
    raise Exception("Unknown format!")
