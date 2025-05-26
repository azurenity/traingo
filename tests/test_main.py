import unittest
from src.main import app # Assuming your Flask app instance is named 'app' in main.py

class TestMain(unittest.TestCase):
    def test_app_creation(self):
        """Test if the Flask app instance is created."""
        self.assertIsNotNone(app, "Flask app should be created and not None.")

if __name__ == '__main__':
    unittest.main() 