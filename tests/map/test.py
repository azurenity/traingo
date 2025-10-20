import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import src.station_path as station_path
from src.station_path import MRT_travel_algo 
import unittest

class TestMRTAlgorithm(unittest.TestCase):
    def test_shortest_path_algo(self):
        # Arrange: small deterministic graph
        station_path.MRT_stations = ['A', 'B', 'C']
        station_path.adj_dict = {
            'A': [('B', 5), ('C', 10)],
            'B': [('C', 3)],
            'C': []
        }

        # Act
        result = MRT_travel_algo('A', 'C')

        # Assert
        expected = 'Time to reach the station including transfer timing is 8 minutes and path taken is A --> B --> C'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()