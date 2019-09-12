.PHONY: test clean-all clean-pyc clean-build

test:
	tox

clean-pyc:
	find -type f -name *.pyc -delete

clean-build:
	rm -rf build/ dist/ *.egg-info  .coverage* .pytest_cache .tox

clean: clean-pyc clean-build

clean-all: clean-pyc clean-build
	rm -rf .tox

package:
	virtualenv .venv --python python3
	.venv/bin/pip install setuptools wheel
	.venv/bin/python3 setup.py sdist bdist_wheel
