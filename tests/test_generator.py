from gendiff import generate_diff
from gendiff.scripts.generator_script import main
import random


filepaths1 = ["tests/fixtures/bigfile1.json", "tests/fixtures/bigfile1.yaml"]
filepaths2 = ["tests/fixtures/bigfile2.json", "tests/fixtures/bigfile2.yaml"]
result_filepaths = ["tests/fixtures/stylish_view_result.txt",
                    "tests/fixtures/plain_view_result.txt",
                    "tests/fixtures/json_view_result.txt"]
format_names = ["stylish", "plain", "json"]


def test_cli(capsys):
    filepath1 = random.choice(filepaths1)
    filepath2 = random.choice(filepaths2)
    format_name = random.choice(format_names)
    correct_answer_path = get_correct_answer_path(format_name)
    correct_answer = open(correct_answer_path).read()
    main([filepath1, filepath2, "-f", format_name])
    captured = capsys.readouterr()
    if "stylish" in format_name:
        assert captured.out == correct_answer + "\n"
    elif "plain" in format_name:
        assert captured.out == correct_answer + "\n"
    elif "json" in format_name:
        assert captured.out == correct_answer + "\n"


def test_json_files():
    json_filepath1 = "tests/fixtures/bigfile1.json"
    json_filepath2 = "tests/fixtures/bigfile2.json"
    stylish_result = open("tests/fixtures/stylish_view_result.txt").read()
    plain_result = open("tests/fixtures/plain_view_result.txt").read()
    json_result = open("tests/fixtures/json_view_result.txt").read()
    assert generate_diff(json_filepath1, json_filepath2, "stylish") == stylish_result
    assert generate_diff(json_filepath1, json_filepath2, "plain") == plain_result
    assert generate_diff(json_filepath1, json_filepath2, "json") == json_result


def test_yaml_files():
    yaml_filepath1 = "tests/fixtures/bigfile1.yaml"
    yaml_filepath2 = "tests/fixtures/bigfile2.yaml"
    stylish_result = open("tests/fixtures/stylish_view_result.txt").read()
    plain_result = open("tests/fixtures/plain_view_result.txt").read()
    json_result = open("tests/fixtures/json_view_result.txt").read()
    assert generate_diff(yaml_filepath1, yaml_filepath2, "stylish") == stylish_result
    assert generate_diff(yaml_filepath1, yaml_filepath2, "plain") == plain_result
    assert generate_diff(yaml_filepath1, yaml_filepath2, "json") == json_result


def get_correct_answer_path(format_name):
    for elem in result_filepaths:
        if format_name in elem:
            return elem
    