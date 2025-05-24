#!/bin/bash
# Script to run pytest tests, ensuring src module is found.

echo "Setting PYTHONPATH to current directory and running tests..."

# Export PYTHONPATH for the current shell session
export PYTHONPATH=.

# Run pytest
pytest

# Optional: Unset PYTHONPATH if you want to clean up, though it's usually not necessary for a script
# unset PYTHONPATH

echo "Tests finished." 