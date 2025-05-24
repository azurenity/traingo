import unittest
import json
from src.main import app # Your Flask app from main.py

class TestStatusAPI(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the Flask app."""
        app.testing = True
        self.client = app.test_client()

    def test_status_endpoint(self):
        """Test the /api/v1/status endpoint."""
        response = self.client.get('/api/v1/status')
        self.assertEqual(response.status_code, 200, "Should return 200 OK")
        
        # Parse the JSON response
        data = json.loads(response.data.decode('utf-8'))
        
        # Check the content of the JSON response
        self.assertEqual(data.get('status'), 'OK')
        self.assertEqual(data.get('message'), 'Traingo API is running from status_api blueprint!')

if __name__ == '__main__':
    unittest.main() 