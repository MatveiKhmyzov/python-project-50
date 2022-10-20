install:
		poetry install
start:
		poetry run gendiff /home/matveik/dev_work/projects/file1.yaml /home/matveik/dev_work/projects/file2.yaml
build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install dist/*.whl

package-reinstall:
		python3 -m pip install --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install start build publish package-install lint test test-coverage