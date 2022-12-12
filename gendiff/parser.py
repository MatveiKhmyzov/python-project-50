from gendiff.formats.formatter import get_formatted_data
from os import path
import json
import yaml


NOT_CHANGED = "not changed"
ADD = "add"
DELETE = "delete"
UPDATED = "updated"
NESTED = "nested"


def convert_in_dict(path_file):
    file_extension = path.splitext(path_file)[1]
    return read_file(path_file, file_extension)


def read_file(file, file_extension):
    if file_extension == ".json":
        return json.load(open(file))
    if file_extension == ".yaml" or file_extension == ".yml":
        return yaml.load(open(file), Loader=yaml.SafeLoader)
    else:
        raise Exception("Unknown extension!")


def get_tree(node):
    res = []
    if type(node) is dict:
        for key in node.keys():
            res.append(create_node(key, NOT_CHANGED, get_tree(node[key])))
        return res
    else:
        return node


def generate_diff(path_file1, path_file2, format_name="stylish"):
    file1 = convert_in_dict(path_file1)
    file2 = convert_in_dict(path_file2)
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
            diff_tree.append(create_node(key, DELETE, get_tree(file1[key])))
        elif key not in file1:
            diff_tree.append(create_node(key, ADD, get_tree(file2[key])))
        elif type(file1[key]) == dict and type(file2[key]) == dict:
            diff_tree.append(create_node(key, NESTED,
                                         get_diff(file1[key], file2[key])))
        elif file1[key] == file2[key]:
            diff_tree.append(create_node(key, NOT_CHANGED,
                                         get_tree(file1[key])))
        else:
            diff_tree.append(create_node(key, UPDATED, get_tree(file1[key]),
                                         updated_value=get_tree(file2[key])))
    return diff_tree
