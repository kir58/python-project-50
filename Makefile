sync:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

install: sync build package-install

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report term --cov-report xml

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

check: test lint

.PHONY: sync build package-install install test test-coverage lint lint-fix check
