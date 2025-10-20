import sys, os
import pytest

# Allow importing from src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import src.station_path as station_path
from src.station_path import MRT_travel_algo


@pytest.fixture
def sample_graph(monkeypatch):
    """Fixture to provide a mock MRT graph."""
    # Mock the stations (if needed by MRT_travel_algo)
    monkeypatch.setattr(station_path, "MRT_stations", ["A", "B", "C"])

    # Create deterministic adjacency dictionary
    adj_dict = {
        'A': [('B', 5), ('C', 10)],
        'B': [('C', 3)],
        'C': []
    }
    monkeypatch.setattr(station_path, "adj_dict", adj_dict)
    return adj_dict


def test_shortest_path_algo(sample_graph):
    """Tests the shortest path algorithm on a small fixed graph."""
    result = MRT_travel_algo("A", "C")
    expected = (
        "Time to reach the station including transfer timing is 8 minutes "
        "and path taken is A --> B --> C"
    )
    assert result == expected
