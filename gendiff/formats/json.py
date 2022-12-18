from gendiff.formats.validators import format_json_values

# import json


# def get_json(result_dict):
#     valid_dict = get_valid_data(result_dict)
#     return json.dumps(valid_dict, indent=4)


def get_json(file):
    return json_view(file)


def json_view(diff_tree, level_nest=0):  # noqa: C901
    sorted_diff = sorted(diff_tree, key=lambda d: d['name'])
    result_view = '[\n'
    indent = '        '
    for i in range(level_nest):
        indent += '           '
    for d in range(len(sorted_diff)):
        d_len = len(sorted_diff[d])
        dict_elem_count = 0
        result_view += indent[:-4] + "{\n"
        for key, value in sorted_diff[d].items():
            if isinstance(value, list):
                result_view += indent + '"' + key + '"' + ': ' \
                    + json_view(value, level_nest + 1) + indent + "]\n"
            else:
                if isinstance(value, dict):
                    result_view += indent + '"' + key + '"' + ': ' \
                        + format_json_values(value, indent)
                else:
                    result_view += indent + '"' + key + '"' + ': ' \
                        + '"' + format_json_values(value, indent) + '"'
                if dict_elem_count == d_len - 1:
                    result_view += '\n'
                else:
                    result_view += ',' + '\n'
                    dict_elem_count += 1
        if d == len(sorted_diff) - 1:
            result_view += indent[:-4] + "}\n"
        else:
            result_view += indent[:-4] + "},\n"
    if level_nest == 0:
        result_view += "]"
    return result_view
