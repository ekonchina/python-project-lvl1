install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl,

lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build