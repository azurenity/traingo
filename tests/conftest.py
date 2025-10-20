import os
import sys

# Ensure the repository root is on sys.path so tests can import `src.*` directly.
# Placing this in tests/conftest.py applies to the whole test session.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Also add the project's `src` directory so imports like `import apis.status_api`
# (which assume `src/` is on sys.path) will resolve during test collection.
SRC_DIR = os.path.join(ROOT, "src")
if os.path.isdir(SRC_DIR) and SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
