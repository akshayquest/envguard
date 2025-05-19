.PHONY: install test build publish clean

install:
	pip install -e .
	pip install pytest build twine

test:
	pytest

build:
	python -m build

publish:
	twine upload dist/*

clean:
	rm -rf dist/ build/ *.egg-info
