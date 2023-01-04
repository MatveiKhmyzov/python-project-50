from gendiff.utils.constants import NOT_CHANGED, ADD, DELETE, UPDATED, NESTED


def get_stylish(file):
    return stylish(file)


def stylish(diff_tree, level_nest=0):  # noqa: C901
    sorted_diff = sorted(diff_tree, key=lambda d: d['name'])
    result_view = '{\n'
    indent = '  '
    for i in range(level_nest):
        indent += '    '
    for node in sorted_diff:
        if node['type'] == NOT_CHANGED:
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == DELETE:
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
        if node['type'] == ADD:
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
        if node['type'] == NESTED:
            value = stylish(node['children'], level_nest + 1)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == UPDATED:
            value = format_stylish_values(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
            value = format_stylish_values(node['new_value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
    result_view += indent[:-2] + '}'
    return result_view


def format_stylish_values(node, indent):
    if isinstance(node, dict):
        indent += '    '
        node_view = '{\n'
        for key in node.keys():
            value = format_stylish_values(node[key], indent)
            node_view += indent + '  ' + key + ': ' + value + '\n'
        node_view += indent[:-2] + '}'
    else:
        if isinstance(node, bool):
            node_view = str(node).lower()
        elif node is None:
            node_view = "null"
        else:
            node_view = str(node)
    return node_view
