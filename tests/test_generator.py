from gendiff import generate_diff, reader, get_formatted_data


def test_json_files():
    jsonfile_path1 = "tests/fixtures/file1.json"
    jsonfile_path2 = "tests/fixtures/file2.json"
    file1, file2 = reader(jsonfile_path1, jsonfile_path2)
    result = open("tests/fixtures/json_result.txt").read()
    assert get_formatted_data(generate_diff(file1, file2), "stylish") == result


def test_complex_json_files():
    complex_json_filepath1 = "tests/fixtures/bigfile1.json"
    complex_json_filepath2 = "tests/fixtures/bigfile2.json"
    file1, file2 = reader(complex_json_filepath1, complex_json_filepath2)
    result = open("tests/fixtures/big_json_result.txt").read()
    assert get_formatted_data(generate_diff(file1, file2), "stylish") == result


def test_yaml_files():
    yamlfile_path1 = "tests/fixtures/file1.yaml"
    yamlfile_path2 = "tests/fixtures/file2.yaml"
    file1, file2 = reader(yamlfile_path1, yamlfile_path2)
    result = open("tests/fixtures/yaml_result.txt").read()
    assert get_formatted_data(generate_diff(file1, file2), "stylish") == result


def test_complex_yaml_files():
    complex_yaml_filepath1 = "tests/fixtures/bigfile1.yaml"
    complex_yaml_filepath2 = "tests/fixtures/bigfile2.yaml"
    file1, file2 = reader(complex_yaml_filepath1, complex_yaml_filepath2)
    result = open("tests/fixtures/big_yaml_result.txt").read()
    assert get_formatted_data(generate_diff(file1, file2), "stylish") == result
