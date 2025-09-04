import pytest
from unittest.mock import Mock
from pydantic import ValidationError
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.validators.reserve_table_validator import ReserveTableValidator
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class TestReserveTableValidator:
    
    def test_valid_reservation_data(self, sample_reservation_data):
        # Arrange
        http_request = HttpRequest(sample_reservation_data)
        
        # Act & Assert (should not raise exception)
        ReserveTableValidator(http_request)
    
    def test_valid_reservation_data_with_flask_request(self, sample_reservation_data):
        # Arrange
        mock_request = Mock()
        mock_request.get_json.return_value = sample_reservation_data
        http_request = HttpRequest(mock_request)
        
        # Act & Assert (should not raise exception)
        ReserveTableValidator(http_request)
    
    def test_invalid_body_type_string(self):
        # Arrange
        http_request = HttpRequest("not a dict")
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError, match="Request body must be a JSON object"):
            ReserveTableValidator(http_request)
    
    def test_invalid_body_type_list(self):
        # Arrange
        http_request = HttpRequest([1, 2, 3])
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError, match="Request body must be a JSON object"):
            ReserveTableValidator(http_request)
    
    def test_missing_table_number(self):
        # Arrange
        incomplete_data = {
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_missing_booking_date(self):
        # Arrange
        incomplete_data = {
            "table_number": 1,
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_missing_scheduled_time(self):
        # Arrange
        incomplete_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "customer_id": 1
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_missing_customer_id(self):
        # Arrange
        incomplete_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30"
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_invalid_table_number_string(self):
        # Arrange
        invalid_data = {
            "table_number": "1",  # Should be int
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_invalid_customer_id_string(self):
        # Arrange
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": "1"  # Should be int
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_booking_date_too_short(self):
        # Arrange
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-1-1",  # Too short
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_booking_date_too_long(self):
        # Arrange
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25T",  # Too long
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_scheduled_time_too_short(self):
        # Arrange
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "7:30",  # Too short
            "customer_id": 1
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_scheduled_time_too_long(self):
        # Arrange
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30:00",  # Too long
            "customer_id": 1
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            ReserveTableValidator(http_request)
    
    def test_edge_case_valid_times(self):
        # Arrange - Test edge cases that should be valid
        valid_data = {
            "table_number": 1,
            "booking_date": "2024-01-01",
            "scheduled_time": "00:00",
            "customer_id": 1
        }
        http_request = HttpRequest(valid_data)
        
        # Act & Assert (should not raise exception)
        ReserveTableValidator(http_request)
