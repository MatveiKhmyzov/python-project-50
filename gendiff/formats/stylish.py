def get_stylish(file):
    return stylish(file)


def get_valid_data(result_dict):
    for key, value in result_dict.items():
        if type(result_dict[key]) is dict:
            get_valid_data(result_dict[key])
        else:
            if type(result_dict[key]) is bool:
                result_dict[key] = str(result_dict[key]).lower()
            if result_dict[key] is None:
                result_dict[key] = "null"
    return result_dict


def stylish(result_dict, level_nest=0):  # noqa: C901
    valid_dict = get_valid_data(result_dict)
    result_view = "{\n"
    indent = '  '
    for i in range(level_nest):
        indent += '    '
    for key in list(valid_dict.keys()):
        if type(valid_dict[key]) is dict:
            if key[:2] != '+ ' and key[:2] != '- ' and key[:2] != '  ':
                result_view += indent + '  ' + key + ': '\
                    + stylish(valid_dict[key], level_nest + 1) + '\n'
            else:
                result_view += indent + key + ': '\
                    + stylish(valid_dict[key], level_nest + 1) + '\n'
        else:
            if key[:2] != '+ ' and key[:2] != '- ' and key[:2] != '  ':
                result_view += indent + '  ' + key + ': '\
                    + str(valid_dict[key]) + '\n'
            else:
                result_view += indent + key + ': ' + str(valid_dict[key]) + '\n'
    if level_nest == 0:
        result_view += indent[:-2] + '}\n'
    else:
        result_view += indent[:-2] + '}'
    return result_view
