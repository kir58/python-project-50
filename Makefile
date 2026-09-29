build:
	uv build

package-install:
	uv tool install dist/*.whl

install: build package-install

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check brain_games --fix