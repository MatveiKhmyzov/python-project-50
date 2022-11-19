def get_stylish(file):
    return stylish(file)


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


def stylish(diff_tree, level_nest=0):  # noqa: C901
    valid_diff = get_valid_data(diff_tree)
    result_view = "{\n"
    indent = '  '
    action = ''
    for i in range(level_nest):
        indent += '    '
    for node in valid_diff:
        if node['action'] == 'not changed':
            action = '  '
        if node['action'] == 'delete' or node['action'] == 'to update':
            action = '- '
        if node['action'] == 'add' or node['action'] == 'updated':
            action = '+ '
        if type(node['children']) is list:
            result_view += indent + action + node['name'] + ': '\
                + stylish(node['children'], level_nest + 1) + '\n'
        else:
            result_view += indent + action + node['name'] + ': '\
                + str(node['children']) + '\n'
    if level_nest == 0:
        result_view += indent[:-2] + '}\n'
    else:
        result_view += indent[:-2] + '}'
    return result_view
