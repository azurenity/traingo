#!/bin/bash
# Script to set up environment and run pytest tests using uv.

echo "Ensuring virtual environment and test dependencies are set up..."

# Create virtual environment using uv if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment with uv..."
  uv venv
fi

echo "Installing/syncing project and test dependencies with uv..."
# This will install the project in editable mode and its test dependencies (like pytest)
# as defined in pyproject.toml [project.optional-dependencies.test]
uv pip install -e .[test]

echo "Setting PYTHONPATH to current directory..."
export PYTHONPATH=.

echo "Running tests with uv run pytest..."
# uv run will execute pytest from the virtual environment managed by uv
uv run pytest

echo "Tests finished." 