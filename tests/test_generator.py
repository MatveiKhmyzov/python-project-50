from gendiff import generate_diff, reader, get_formatted_data


def test_stylish_json_files():
    json_filepath1 = "tests/fixtures/bigfile1.json"
    json_filepath2 = "tests/fixtures/bigfile2.json"
    stylish_result = open("tests/fixtures/stylish_view_result.txt").read()
    plain_result = open("tests/fixtures/plain_view_result.txt").read()
    json_result = open("tests/fixtures/json_view_result.txt").read()
    assert get_formatted_data(generate_diff(json_filepath1, json_filepath2), "stylish") == stylish_result
    assert get_formatted_data(generate_diff(json_filepath1, json_filepath2), "plain") == plain_result
    assert get_formatted_data(generate_diff(json_filepath1, json_filepath2), "json") == json_result


def test_stylish_yaml_files():
    yaml_filepath1 = "tests/fixtures/bigfile1.yaml"
    yaml_filepath2 = "tests/fixtures/bigfile2.yaml"
    stylish_result = open("tests/fixtures/stylish_view_result.txt").read()
    plain_result = open("tests/fixtures/plain_view_result.txt").read()
    json_result = open("tests/fixtures/json_view_result.txt").read()
    assert get_formatted_data(generate_diff(yaml_filepath1, yaml_filepath2), "stylish") == stylish_result
    assert get_formatted_data(generate_diff(yaml_filepath1, yaml_filepath2), "plain") == plain_result
    assert get_formatted_data(generate_diff(yaml_filepath1, yaml_filepath2), "json") == json_result
