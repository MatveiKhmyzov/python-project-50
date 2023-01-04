import json
import yaml
from os import path


def read_file(path_file):
    with open(path_file) as f:
        string_data = f.read()
    return string_data


def get_data_format(path_file):
    data_format = path.splitext(path_file)[1]
    return data_format


def convert_in_dict(string_data, data_format):
    if data_format == ".json":
        return json.loads(string_data)
    if data_format == ".yaml" or data_format == ".yml":
        return yaml.load(string_data, Loader=yaml.SafeLoader)
    else:
        raise Exception("Unknown extension!")
