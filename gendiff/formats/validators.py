def format_json_values(node, indent):  # noqa: C901e
    if isinstance(node, dict):
        indent += '    '
        elem_count = 0
        node_view = '{\n'
        for key, value in node.items():
            if isinstance(value, dict) or isinstance(value, int):
                node_view += indent + '"' + str(key) + '"' + ': ' \
                    + format_json_values(value, indent)
            else:
                node_view += indent + '"' + str(key) + '"' + ': ' \
                    + '"' + format_json_values(value, indent) + '"'
            if elem_count == len(node) - 1:
                node_view += "\n"
            else:
                node_view += "," + "\n"
                elem_count += 1
        node_view += indent[:-4] + '}'
    else:
        if isinstance(node, bool):
            node_view = str(node).lower()
        elif node is None:
            node_view = "null"
        else:
            node_view = str(node)
    return node_view


def format_plain_values(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    elif value == '[complex value]':
        value = '[complex value]'
    elif isinstance(value, str):
        value = "'{}'".format(value)
    else:
        value = "{}".format(value)
    return value


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
