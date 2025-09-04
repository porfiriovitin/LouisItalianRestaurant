import pytest
import sys
import os
from unittest.mock import Mock

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def mock_db_connection():
    """Mock database connection for testing"""
    mock_connection = Mock()
    mock_session = Mock()
    mock_connection.session = mock_session
    mock_connection.__enter__ = Mock(return_value=mock_connection)
    mock_connection.__exit__ = Mock(return_value=None)
    return mock_connection

@pytest.fixture
def sample_customer_data():
    """Sample customer data for testing"""
    return {
        "customer_name": "John Doe",
        "cpf": "12345678901",
        "cellphone": "11987654321"
    }

@pytest.fixture
def sample_reservation_data():
    """Sample reservation data for testing"""
    return {
        "table_number": 1,
        "booking_date": "2024-12-25",
        "scheduled_time": "19:30",
        "customer_id": 1
    }

@pytest.fixture
def mock_http_request():
    """Mock HTTP request for testing"""
    class MockRequest:
        def __init__(self, body=None, param=None):
            self.body = body or {}
            self.param = param or {}
    
    return MockRequest
