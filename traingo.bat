@echo off
REM Batch script to run the Traingo Flask application

REM Get the directory where the script is located and change to it
cd /D "%~dp0"

echo Starting Traingo Flask application from src/main.py...

REM Run the Python Flask application
REM Ensure Python is in your PATH and your virtual environment (if any) is activated,
REM or that the 'python' command points to the correct interpreter with Flask installed.
uv run -m src.main

REM If the window closes immediately upon an error before Flask starts,
REM you can uncomment the line below to see the error message.
REM pause 
