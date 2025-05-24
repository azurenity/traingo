@echo off
REM Script to set up environment and run pytest tests on Windows using uv.

echo Ensuring virtual environment and test dependencies are set up...

REM Create virtual environment using uv if it doesn't exist
if not exist .venv (
    echo Creating virtual environment with uv...
    uv venv
)

echo Installing/syncing project and test dependencies with uv...
REM This will install the project in editable mode and its test dependencies (like pytest)
REM as defined in pyproject.toml [project.optional-dependencies.test]
uv pip install -e .[test]

echo Setting PYTHONPATH to current directory...
set PYTHONPATH=.

echo Running tests with uv run pytest...
REM uv run will execute pytest from the virtual environment managed by uv
uv run pytest

echo Tests finished. 