from gendiff.formats.validators import get_valid_data


def get_json(result_dict, level_nest=0):  # noqa: C901
    valid_dict = get_valid_data(result_dict)
    result_view = '[\n'
    indent = '  '
    for i in range(level_nest):
        indent += '              '
    for d in range(len(valid_dict)):
        d_len = len(valid_dict[d])
        dict_elem_count = 0
        result_view += indent[:-1] + "{\n"
        for key, value in valid_dict[d].items():
            if type(value) is list:
                result_view += indent + '"' + key + '"' + ': ' \
                    + get_json(value, level_nest + 1)
                dict_elem_count += 1
            else:
                if dict_elem_count == d_len - 1:
                    result_view += indent + '"' + key + '"' + ': '\
                        + '"' + str(value) + '"' + '\n'
                else:
                    result_view += indent + '"' + key + '"' + ': '\
                        + '"' + str(value) + '"' + ',' + '\n'
                    dict_elem_count += 1
        if d == len(valid_dict) - 1:
            result_view += indent[:-1] + "}\n"
        else:
            result_view += indent[:-1] + "},\n"
    if level_nest != 0:
        result_view += indent[:-2] + "]\n"
    else:
        result_view += indent[:-2] + "]"
    return result_view
