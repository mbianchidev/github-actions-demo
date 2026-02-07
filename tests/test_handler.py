"""
Tests for the Lambda handler module.
"""

from typing import Any, Dict

from src.handler import lambda_handler


def test_lambda_handler_returns_success() -> None:
    """Test that the lambda handler returns a successful response."""
    event: Dict[str, Any] = {}
    context = None

    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    assert "Hello from GitHub Actions Demo Lambda!" in response["body"]
    assert response["headers"]["Content-Type"] == "application/json"


def test_lambda_handler_processes_event() -> None:
    """Test that the lambda handler processes the event correctly."""
    event: Dict[str, Any] = {"test_key": "test_value"}
    context = None

    response = lambda_handler(event, context)

    assert response["statusCode"] == 200
    assert isinstance(response["body"], str)
