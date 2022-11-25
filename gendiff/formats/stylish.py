from gendiff.formats.validators import get_valid_data


def get_stylish(file):
    return stylish(file)


def stylish(diff_tree, level_nest=0):  # noqa: C901
    valid_diff = get_valid_data(diff_tree)
    result_view = '{\n'
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
        if node['type'] == 'internal node':
            result_view += indent + action + node['name'] + ': '\
                + stylish(node['children'], level_nest + 1) + '\n'
        else:
            result_view += indent + action + node['name'] + ': '\
                + str(node['value']) + '\n'
    if level_nest == 0:
        result_view += indent[:-2] + '}\n'
    else:
        result_view += indent[:-2] + '}'
    return result_view
