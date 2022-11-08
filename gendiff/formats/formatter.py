from gendiff.formats.stylish import get_stylish


def get_formatted_data(file, name_format):
    if name_format == "stylish":
        return get_stylish(file)
    else:
        print("Unknown format!")
        return get_stylish(file)
