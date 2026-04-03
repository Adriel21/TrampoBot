.PHONY: install dev run

install:
	uv venv
	uv sync

dev:
	uv sync --extra dev

run:
	uvicorn trampobot.main:app --reload