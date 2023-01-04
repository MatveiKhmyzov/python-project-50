from gendiff.formats.formatter import get_formatted_data
from gendiff.utils.diff import get_diff
from gendiff.utils.parser import read_file, get_data_format, convert_in_dict


def generate_diff(path_file1, path_file2, format_name="stylish"):
    text_file1 = read_file(path_file1)
    text_file2 = read_file(path_file2)
    data_format1 = get_data_format(path_file1)
    data_format2 = get_data_format(path_file2)
    file1 = convert_in_dict(text_file1, data_format1)
    file2 = convert_in_dict(text_file2, data_format2)
    diff_tree = get_diff(file1, file2)
    return get_formatted_data(diff_tree, format_name)
