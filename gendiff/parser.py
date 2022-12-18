from gendiff.formats.formatter import get_formatted_data
from os import path
import json
import yaml


NOT_CHANGED = "not changed"
ADD = "add"
DELETE = "delete"
UPDATED = "updated"
NESTED = "nested"


def read_file(path_file):
    with open(path_file) as f:
        string_data = f.read()
    return string_data


def get_data_format(path_file):
    data_format = path.splitext(path_file)[1]
    return data_format


def convert_in_dict(string_data, data_format):
    if data_format == ".json":
        return json.loads(string_data)
    if data_format == ".yaml" or data_format == ".yml":
        return yaml.load(string_data, Loader=yaml.SafeLoader)
    else:
        raise Exception("Unknown extension!")


def generate_diff(path_file1, path_file2, format_name="stylish"):
    text_file1 = read_file(path_file1)
    text_file2 = read_file(path_file2)
    data_format1 = get_data_format(path_file1)
    data_format2 = get_data_format(path_file2)
    file1 = convert_in_dict(text_file1, data_format1)
    file2 = convert_in_dict(text_file2, data_format2)
    diff_tree = get_diff(file1, file2)
    return get_formatted_data(diff_tree, format_name)


def create_node(name=None, state_type=None,
                value=None, updated_value="smthng"):
    node = {
        'name': name,
        'type': state_type,
    }
    if state_type == 'nested':
        node['children'] = value
    else:
        node['value'] = value
    if updated_value != "smthng":
        node["new_value"] = updated_value
    elif updated_value is None:
        node["new_value"] = updated_value
    return node


def get_diff(file1, file2):
    union_keys = (file1.keys() | file2.keys())
    diff_tree = []
    for key in union_keys:
        if key not in file2:
            diff_tree.append(create_node(key, DELETE, file1[key]))
        elif key not in file1:
            diff_tree.append(create_node(key, ADD, file2[key]))
        elif type(file1[key]) == dict and type(file2[key]) == dict:
            diff_tree.append(create_node(key, NESTED,
                                         get_diff(file1[key], file2[key])))
        elif file1[key] == file2[key]:
            diff_tree.append(create_node(key, NOT_CHANGED,
                                         file1[key]))
        else:
            diff_tree.append(create_node(key, UPDATED, file1[key],
                                         updated_value=file2[key]))
    return diff_tree
