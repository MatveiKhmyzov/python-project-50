

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
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    elif value == '[complex value]':
        value = '[complex value]'
    else:
        value = "'{}'".format(value)
    return value
