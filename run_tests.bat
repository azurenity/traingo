@echo off
REM Script to run pytest tests on Windows, ensuring src module is found.

echo Setting PYTHONPATH to current directory and running tests...

REM Set PYTHONPATH for the current command prompt session
set PYTHONPATH=.

REM Run pytest
pytest

REM Optional: Clear PYTHONPATH if you want to clean up
REM set PYTHONPATH=

echo Tests finished. 