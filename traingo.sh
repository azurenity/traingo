#!/bin/bash

# Script to run the Traingo Flask application

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Change to the script's directory (project root)
cd "$SCRIPT_DIR"

echo "Starting Traingo Flask application from src/main.py..."

# Run the Python Flask application
# Ensure your virtual environment (if you use one, like .venv) is activated
# or that python3 points to the correct interpreter with Flask installed.
python src/main.py 
