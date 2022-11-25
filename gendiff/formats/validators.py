

def get_valid_data(diff_tree):
    for node in diff_tree:
        if type(node['children']) is list:
            get_valid_data(node['children'])
        else:
            if type(node['children']) is bool:
                node['children'] = str(node['children']).lower()
            if node['children'] is None:
                node['children'] = "null"
    return diff_tree


def get_format_values(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if value == "[complex value]":
        return "[complex value]"
    else:
        return "'{}'".format(value)
