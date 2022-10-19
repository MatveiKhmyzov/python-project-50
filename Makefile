install:
		poetry install
start:
		poetry run gendiff /home/matveik/dev_work/projects/file1.json /home/matveik/dev_work/projects/file2.json
build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

.PHONY: install start build publish package-install lint test