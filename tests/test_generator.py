from gendiff import generate_diff


def test_json_files():
    jsonfile_path1 = "tests/fixtures/file1.json"
    jsonfile_path2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/json_result.txt").read()
    assert generate_diff(jsonfile_path1, jsonfile_path2) == result


def test_yaml_files():
    yamlfile_path1 = "tests/fixtures/file1.yaml"
    yamlfile_path2 = "tests/fixtures/file2.yaml"
    result = open("tests/fixtures/yaml_result.txt").read()
    assert generate_diff(yamlfile_path1, yamlfile_path2) == result
