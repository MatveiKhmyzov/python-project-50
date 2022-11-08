import json
import yaml


def reader(file_path1, file_path2):
    if ".json" in file_path1:
        first_file = json.load(open(file_path1))
        second_file = json.load(open(file_path2))
    else:
        first_file = yaml.load(open(file_path1), Loader=yaml.SafeLoader)
        second_file = yaml.load(open(file_path2), Loader=yaml.SafeLoader)
    return first_file, second_file


def sort_dict(result_dict, file1, file2):
    only_first_file_keys = (list(file1.keys() - file2.keys()))
    only_second_file_keys = (list(file2.keys() - file1.keys()))

    return {k: sort_dict(v, file1, file2) if isinstance(v, dict)
            and k[2:] not in (set(only_first_file_keys) | set(only_second_file_keys))  # noqa: W503, E501
            else v for k, v
            in sorted(result_dict.items(), key=lambda x: x[0][2:])}


def generate_diff(file1, file2):  # noqa: C901
    union_keys = (list(file1.keys() & file2.keys()))
    only_first_file_keys = (list(file1.keys() - file2.keys()))
    only_second_file_keys = (list(file2.keys() - file1.keys()))
    result_dict = {}
    for elem in union_keys:
        if file1[elem] == file2[elem]:
            result_dict['  ' + elem] = str(file1[elem])
        if file1[elem] != file2[elem]:
            if type(file1[elem]) == dict and type(file2[elem]) == dict:
                result_dict['  ' + elem] = generate_diff(file1[elem],
                                                         file2[elem])
            else:
                result_dict['- ' + elem] = file1[elem]
                result_dict['+ ' + elem] = file2[elem]
    for i in only_first_file_keys:
        result_dict[('- ' + i)] = file1[i]
    for i in only_second_file_keys:
        result_dict[('+ ' + i)] = file2[i]

    return sort_dict(result_dict, file1, file2)
