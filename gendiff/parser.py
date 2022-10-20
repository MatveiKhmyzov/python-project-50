import json
import yaml


def change_order_single_tuples(item):
    for i in range(len(item) - 1):
        if item[i][0] == item[i + 1][0]:
            item[i], item[i + 1] = item[i + 1], item[i]
    return item


def change_capital_word(iter_obj):
    for key in iter_obj:
        if type(iter_obj[key]) is bool:
            iter_obj[key] = str(iter_obj[key]).lower()
    return iter_obj


def generate_diff(file_path1, file_path2):
    if ".json" in file_path1:
        first_file = change_capital_word(json.load(open(file_path1)))
        second_file = change_capital_word(json.load(open(file_path2)))
    first_file = change_capital_word(yaml.load(open(file_path1), Loader=yaml.SafeLoader))
    second_file = change_capital_word(yaml.load(open(file_path2), Loader=yaml.SafeLoader))
    first_set = set(first_file.items())
    second_set = set(second_file.items())
    union = first_set | second_set
    union_lst = [list(i) for i in union]
    result_lst = change_order_single_tuples(sorted(union_lst))
    answer_lst = []
    for elem in result_lst:
        if tuple(elem) in first_set and tuple(elem) in second_set:
            answer_lst.append("".join(f"    {elem[0]}: {elem[1]}"))
        elif tuple(elem) in first_set and tuple(elem) not in second_set:
            answer_lst.append("".join(f"  - {elem[0]}: {elem[1]}"))
        elif tuple(elem) in second_set and tuple(elem) not in first_set:
            answer_lst.append("".join(f"  + {elem[0]}: {elem[1]}"))
    return "{0}\n{1}\n{2}\n".format('{', "\n".join(answer_lst), '}')
