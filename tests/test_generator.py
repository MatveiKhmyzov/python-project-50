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
    filepath1 = random.choice(filepaths1)
    filepath2 = random.choice(filepaths2)
    format_name = random.choice(format_names)
    correct_answer_path = get_correct_answer_path(format_name)
    correct_answer = open(correct_answer_path).read()
    if "stylish" in format_name:
        assert generate_diff(filepath1, filepath2, format_name) == correct_answer
    elif "plain" in format_name:
        assert generate_diff(filepath1, filepath2, format_name) == correct_answer
    elif "json" in format_name:
        assert generate_diff(filepath1, filepath2, format_name) == correct_answer


def get_correct_answer_path(format_name):
    for elem in result_filepaths:
        if format_name in elem:
            return elem
