from gendiff.formats.validators import format_stylish_values


def get_stylish(file):
    return stylish(file)


def stylish(diff_tree, level_nest=0):  # noqa: C901
    sorted_diff = sorted(diff_tree, key=lambda d: d['name'])
    result_view = '{\n'
    indent = '  '
    for i in range(level_nest):
        indent += '    '
    for node in sorted_diff:
        if node['type'] == 'not changed':
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == 'delete':
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
        if node['type'] == 'add':
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
        if 'children' in node:
            value = stylish(node['children'], level_nest + 1)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == 'updated':
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
            value = format_stylish_values(node['new_value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
    result_view += indent[:-2] + '}'
    return result_view
