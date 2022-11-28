from gendiff.formats.formatter import get_formatted_data
import json
import yaml


def reader(path_file):
    if ".json" in path_file:
        return json.load(open(path_file))
    else:
        return yaml.load(open(path_file), Loader=yaml.SafeLoader)


def get_tree(node):
    res = []
    for key in node.keys():
        if type(node[key]) is dict:
            res.append({
                'name': key,
                'action': 'not changed',
                'type': 'internal node',
                'children': get_tree(node[key])
            })
        else:
            res.append({
                'name': key,
                'action': 'not changed',
                'type': 'leaf',
                'value': node[key]
            })
    return res


def sort_diff(diff_tree):
    sorted_dict = sorted(diff_tree, key=lambda d: d['name'])
    for item in sorted_dict:
        if item['type'] == 'internal node':
            item['children'] = sort_diff(item['children'])
    return sorted_dict


def generate_diff(path_file1, path_file2, format_name="stylish"):
    file1 = reader(path_file1)
    file2 = reader(path_file2)
    diff_tree = get_diff(file1, file2)
    return get_formatted_data(diff_tree, format_name)


def get_diff(file1, file2):  # noqa: C901
    union_keys = list(file1.keys() & file2.keys())
    only_first_file_keys = list(file1.keys() - file2.keys())
    only_second_file_keys = list(file2.keys() - file1.keys())
    diff_tree = []
    for key in union_keys:
        if file1[key] == file2[key]:
            diff_tree.append({
                'name': key,
                'action': 'not changed',
                'type': 'leaf',
                'value': file1[key]
            })
        if file1[key] != file2[key]:
            if type(file1[key]) == dict and type(file2[key]) == dict:
                diff_tree.append({
                    'name': key,
                    'action': 'not changed',
                    'type': 'internal node',
                    'children': get_diff(file1[key], file2[key])
                })
            else:
                if type(file1[key]) == dict:
                    diff_tree.append({
                        'name': key,
                        'action': 'to update',
                        'type': 'internal node',
                        'children': get_tree(file1[key])
                    })
                else:
                    diff_tree.append({
                        'name': key,
                        'action': 'to update',
                        'type': 'leaf',
                        'value': file1[key]
                    })
                if type(file2[key]) == dict:
                    diff_tree.append({
                        'name': key,
                        'action': 'updated',
                        'type': 'internal node',
                        'children': get_tree(file2[key])
                    })
                else:
                    diff_tree.append({
                        'name': key,
                        'action': 'updated',
                        'type': 'leaf',
                        'value': file2[key]
                    })

    for key in only_first_file_keys:
        if type(file1[key]) is dict:
            diff_tree.append({
                'name': key,
                'action': 'delete',
                'type': 'internal node',
                'children': get_tree(file1[key])
            })
        else:
            diff_tree.append({
                'name': key,
                'action': 'delete',
                'type': 'leaf',
                'value': file1[key]
            })
    for key in only_second_file_keys:
        if type(file2[key]) is dict:
            diff_tree.append({
                'name': key,
                'action': 'add',
                'type': 'internal node',
                'children': get_tree(file2[key])
            })
        else:
            diff_tree.append({
                'name': key,
                'action': 'add',
                'type': 'leaf',
                'value': file2[key]
            })

    return sort_diff(diff_tree)
