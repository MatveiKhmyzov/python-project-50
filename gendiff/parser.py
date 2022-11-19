import json
import yaml


def reader(file_path1, file_path2):
    if ".json" in file_path1:
        first_file = json.load(open(file_path1))
        second_file = json.load(open(file_path2))
    else:
        first_file = yaml.load(open(file_path1), Loader=yaml.SafeLoader)
        second_file = yaml.load(open(file_path2), Loader=yaml.SafeLoader)
    return first_file, second_file


def get_tree(node):
    res = []
    for key in node.keys():
        if type(node[key]) is dict:
            res.append({
                'name': key,
                'children': get_tree(node[key]),
                'action': 'not changed',
                'type': 'internal node'
            })
        else:
            res.append({
                'name': key,
                'children': node[key],
                'action': 'not changed',
                'type': 'leaf'
            })
    return res


def sort_diff(diff_tree):
    sorted_dict = sorted(diff_tree, key=lambda d: d['name'])
    for item in sorted_dict:
        if type(item['children']) is list:
            item['children'] = sort_diff(item['children'])
    return sorted_dict


def generate_diff(file1, file2):  # noqa: C901
    union_keys = list(file1.keys() & file2.keys())
    only_first_file_keys = list(file1.keys() - file2.keys())
    only_second_file_keys = list(file2.keys() - file1.keys())
    diff_tree = []
    for key in union_keys:
        if file1[key] == file2[key]:
            diff_tree.append({
                'name': key,
                'children': file1[key],
                'action': 'not changed',
                'type': 'leaf'
            })
        if file1[key] != file2[key]:
            if type(file1[key]) == dict and type(file2[key]) == dict:
                diff_tree.append({
                    'name': key,
                    'children': generate_diff(file1[key], file2[key]),
                    'action': 'not changed',
                    'type': 'internal node'
                })
            else:
                if type(file1[key]) == dict:
                    diff_tree.append({
                        'name': key,
                        'children': get_tree(file1[key]),
                        'action': 'to update',
                        'type': 'leaf'
                    })
                else:
                    diff_tree.append({
                        'name': key,
                        'children': file1[key],
                        'action': 'to update',
                        'type': 'leaf'
                    })
                if type(file2[key]) == dict:
                    if key in file1:
                        diff_tree.append({
                            'name': key,
                            'children': get_tree(file2[key]),
                            'action': 'updated',
                            'type': 'leaf',
                        })
                else:
                    if key in file1:
                        diff_tree.append({
                            'name': key,
                            'children': file2[key],
                            'action': 'updated',
                            'type': 'leaf',
                        })

    for key in only_first_file_keys:
        if type(file1[key]) is dict:
            diff_tree.append({
                'name': key,
                'children': get_tree(file1[key]),
                'action': 'delete',
                'type': 'internal node'
            })
        else:
            diff_tree.append({
                'name': key,
                'children': file1[key],
                'action': 'delete',
                'type': 'leaf'
            })
    for key in only_second_file_keys:
        if type(file2[key]) is dict:
            diff_tree.append({
                'name': key,
                'children': get_tree(file2[key]),
                'action': 'add',
                'type': 'internal node'
            })
        else:
            diff_tree.append({
                'name': key,
                'children': file2[key],
                'action': 'add',
                'type': 'leaf'
            })

    return sort_diff(diff_tree)
