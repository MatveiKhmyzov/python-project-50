from gendiff.utils.constants import NOT_CHANGED, ADD, DELETE, UPDATED, NESTED


def create_node(name, state_type, nested_value,
                value, updated_value):
    node = {
        'name': name,
        'type': state_type,
        'children': nested_value,
        'value': value,
        'new_value': updated_value
    }
    return node


def get_diff(file1, file2):
    union_keys = file1.keys() | file2.keys()
    diff_tree = []
    for key in union_keys:
        if key not in file2:
            diff_tree.append(create_node(key, DELETE, None, file1[key], None))
        elif key not in file1:
            diff_tree.append(create_node(key, ADD, None, file2[key], None))
        elif type(file1[key]) == dict and type(file2[key]) == dict:
            diff_tree.append(create_node(key, NESTED,
                             get_diff(file1[key], file2[key]), None, None))
        elif file1[key] == file2[key]:
            diff_tree.append(create_node(key, NOT_CHANGED, None,
                             file1[key], None))
        else:
            diff_tree.append(create_node(key, UPDATED, None, file1[key],
                             file2[key]))
    return diff_tree
