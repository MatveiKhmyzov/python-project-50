from gendiff.formats.validators import get_valid_data

# import json


# def get_json(result_dict):
#     valid_dict = get_valid_data(result_dict)
#     return json.dumps(valid_dict, indent=4)

def get_json(result_dict, level_nest=0):  # noqa: C901
    valid_dict = get_valid_data(result_dict)
    result_view = '[\n'
    indent = '        '
    for i in range(level_nest):
        indent += '           '
    for d in range(len(valid_dict)):
        d_len = len(valid_dict[d])
        dict_elem_count = 0
        result_view += indent[:-4] + "{\n"
        for key, value in valid_dict[d].items():
            leaf_node = indent + '"' + key + '"' + ': '\
                + '"' + str(value) + '"'
            if type(value) is list or isinstance(value, dict):
                nested_node = indent + '"' + key + '"' + ': ' \
                    + get_json(value, level_nest + 1) + indent
                if dict_elem_count == d_len - 1:
                    result_view += nested_node + "]\n"
                else:
                    result_view += nested_node + "],\n"
                    dict_elem_count += 1
            else:
                if dict_elem_count == d_len - 1:
                    result_view += leaf_node + '\n'
                else:
                    result_view += leaf_node + ',' + '\n'
                    dict_elem_count += 1
        if d == len(valid_dict) - 1:
            result_view += indent[:-4] + "}\n"
        else:
            result_view += indent[:-4] + "},\n"
    if level_nest == 0:
        result_view += "]"
    return result_view
