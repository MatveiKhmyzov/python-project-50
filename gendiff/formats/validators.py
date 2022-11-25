

def get_valid_data(diff_tree):
    for node in diff_tree:
        if node['type'] == 'internal node':
            get_valid_data(node['children'])
        else:
            if type(node['value']) is bool:
                node['value'] = str(node['value']).lower()
            if node['value'] is None:
                node['value'] = "null"
    return diff_tree


def get_format_values(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if value == '[complex value]':
        return '[complex value]'
    else:
        return "'{}'".format(value)
