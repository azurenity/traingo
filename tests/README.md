Why tests/conftest.py exists

The tests in this repository import application modules using two styles:

- `from src.<module> import ...` (tests that import the package under `src`) and
- `from apis.<module> import ...` (some application code uses top-level imports assuming `src/` is on PYTHONPATH)

When pytest collects test modules it imports them directly. If the repository root or the `src/` directory isn't on Python's import path, imports such as `import src.main` or `import apis.status_api` will fail during collection with ModuleNotFoundError.

To make tests reproducible for contributors and CI, `tests/conftest.py` adds the repository root and the `src/` directory to `sys.path` prior to collection. This is a deliberate, minimal change so tests can run without requiring an editable installation of the package.

Is this cross-platform?

Yes. `tests/conftest.py` uses only `os.path` and `sys.path` modifications; those work the same on Windows, macOS, and Linux. Adding paths to `sys.path` is a pure-Python operation and is portable.

Alternatives (pick one if you prefer):

1) Editable install (recommended for larger projects)
   - Run:
     ```bash
     python -m pip install -e .[dev]
     ```
   - This installs the package so imports resolve without modifying `sys.path` in tests.

2) Update imports to always use package-qualified names
   - Change application code to use `from src.apis import status_api` rather than `from apis import status_api` and update imports accordingly.

3) Keep `tests/conftest.py` as-is
   - Pros: simplest for contributors and CI, no install step required.
   - Cons: test behavior depends on a runtime `sys.path` tweak. For most projects this is acceptable for test suites.

How to run tests (cross-platform):

- Create a virtual environment (recommended)
  - Windows (PowerShell):
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    # if activation blocked: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\.venv\Scripts\Activate.ps1
    ```
  - macOS / Linux:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

- Install dev dependencies (pytest):
  ```bash
  python -m pip install --upgrade pip
  python -m pip install pytest
  ```

- Run the full test suite from the repo root:
  ```bash
  pytest -q
  ```

- Run a single test file:
  ```bash
  pytest tests/map/test_station_path.py -q
  ```

If you'd like, I can also add a short note to the project `README.md` describing the test workflow. Let me know.