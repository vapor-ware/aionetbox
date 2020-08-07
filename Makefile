.PHONY: unit-test, lint, test-integration, ci-pypi-release

unit-test:
	tox

lint:
	tox -e lint

ci-pypi-release:
	tox -e release
