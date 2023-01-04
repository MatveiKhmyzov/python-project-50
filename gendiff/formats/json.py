import json
from gendiff.constants import ADD, DELETE, UPDATED, NESTED, NOT_CHANGED


def get_json(result_dict):
    return json.dumps(get_clean_diff(result_dict), indent=4)


def sort_diff(diff_tree):
    sorted_dict = sorted(diff_tree, key=lambda d: d['name'])
    for item in sorted_dict:
        if item['type'] == NESTED:
            item['children'] = sort_diff(item['children'])
    return sorted_dict


def get_clean_diff(iterable):
    clean_diff = []
    for dct in iterable:
        clean_node = {
            'name': dct['name'],
            'type': dct['type']
        }
        if dct['type'] == ADD\
                or dct['type'] == DELETE\
                or dct['type'] == NOT_CHANGED:
            clean_node['value'] = dct['value']
        if dct['type'] == UPDATED:
            clean_node['value'] = dct['value']
            clean_node['new_value'] = dct['new_value']
        if dct['type'] == NESTED:
            clean_node['children'] = get_clean_diff(dct['children'])

        clean_diff.append(clean_node)

    return sort_diff(clean_diff)
