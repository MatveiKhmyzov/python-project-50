from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json


STYLISH_FORMAT = 'stylish'
PLAIN_FORMAT = 'plain'
JSON_FORMAT = "json"


def sort_diff(diff_tree):
    sorted_dict = sorted(diff_tree, key=lambda d: d['name'])
    for item in sorted_dict:
        if item['type'] == 'nested':
            item['children'] = sort_diff(item['children'])
    return sorted_dict


def get_formatted_data(file, name_format):
    if name_format == STYLISH_FORMAT:
        return get_stylish(sort_diff(file))
    if name_format == PLAIN_FORMAT:
        return get_plain(sort_diff(file))
    if name_format == JSON_FORMAT:
        return get_json(sort_diff(file))
    raise Exception("Unknown format!")
