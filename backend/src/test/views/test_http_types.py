import pytest
from unittest.mock import Mock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TestHttpRequest:
    
    def test_http_request_with_flask_request(self):
        # Arrange
        mock_flask_request = Mock()
        mock_flask_request.get_json.return_value = {"key": "value"}
        
        # Act
        http_request = HttpRequest(mock_flask_request, {"param1": "value1"})
        
        # Assert
        assert http_request.body == {"key": "value"}
        assert http_request.param == {"param1": "value1"}
    
    def test_http_request_with_flask_request_no_params(self):
        # Arrange
        mock_flask_request = Mock()
        mock_flask_request.get_json.return_value = {"key": "value"}
        
        # Act
        http_request = HttpRequest(mock_flask_request)
        
        # Assert
        assert http_request.body == {"key": "value"}
        assert http_request.param == {}
    
    def test_http_request_with_dict(self):
        # Arrange
        body_data = {"key": "value"}
        
        # Act
        http_request = HttpRequest(body_data, {"param1": "value1"})
        
        # Assert
        assert http_request.body == {"key": "value"}
        assert http_request.param == {"param1": "value1"}
    
    def test_http_request_with_none_json(self):
        # Arrange
        mock_flask_request = Mock()
        mock_flask_request.get_json.return_value = None
        
        # Act
        http_request = HttpRequest(mock_flask_request)
        
        # Assert
        assert http_request.body == {}
        assert http_request.param == {}
    
    def test_http_request_with_flask_request_silent_mode(self):
        # Arrange
        mock_flask_request = Mock()
        mock_flask_request.get_json.return_value = {"data": "test"}
        
        # Act
        http_request = HttpRequest(mock_flask_request)
        
        # Assert
        mock_flask_request.get_json.assert_called_once_with(silent=True)
        assert http_request.body == {"data": "test"}

class TestHttpResponse:
    
    def test_http_response_with_body(self):
        # Act
        response = HttpResponse(status_code=200, body={"message": "success"})
        
        # Assert
        assert response.status_code == 200
        assert response.body == {"message": "success"}
    
    def test_http_response_without_body(self):
        # Act
        response = HttpResponse(status_code=204)
        
        # Assert
        assert response.status_code == 204
        assert response.body is None
    
    def test_http_response_different_status_codes(self):
        # Test various status codes
        responses = [
            HttpResponse(status_code=201, body={"created": True}),
            HttpResponse(status_code=400, body={"error": "Bad Request"}),
            HttpResponse(status_code=404, body={"error": "Not Found"}),
            HttpResponse(status_code=500, body={"error": "Internal Server Error"})
        ]
        
        assert responses[0].status_code == 201
        assert responses[1].status_code == 400
        assert responses[2].status_code == 404
        assert responses[3].status_code == 500
