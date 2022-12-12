def get_stylish(file):
    return stylish(file)


def stylish(diff_tree, level_nest=0):  # noqa: C901
    result_view = '{\n'
    indent = '  '
    for i in range(level_nest):
        indent += '    '
    for node in diff_tree:
        if node['type'] == 'not changed':
            value = prepare_data(node['value'], indent)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == 'delete':
            value = prepare_data(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
        if node['type'] == 'add':
            value = prepare_data(node['value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
        if 'children' in node:
            value = stylish(node['children'], level_nest + 1)
            result_view += f"{indent}  {node['name']}: {value}\n"
        if node['type'] == 'updated':
            value = prepare_data(node['value'], indent)
            result_view += f"{indent}- {node['name']}: {value}\n"
            value = prepare_data(node['new_value'], indent)
            result_view += f"{indent}+ {node['name']}: {value}\n"
    result_view += indent[:-2] + '}'
    return result_view


def prepare_data(node, indent):
    if isinstance(node, list):
        indent += '    '
        node_view = '{\n'
        for elem in node:
            value = prepare_data(elem['value'], indent)
            node_view += indent + '  ' + elem['name'] + ': ' + value + '\n'
        node_view += indent[:-2] + '}'
    else:
        if isinstance(node, bool):
            node_view = str(node).lower()
        elif node is None:
            node_view = "null"
        else:
            node_view = str(node)
    return node_view
