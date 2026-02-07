"""
Lambda handler module for AWS Lambda function.

This module contains the main handler function that processes events.
"""

from typing import Any, Dict


def lambda_handler(
    event: Dict[str, Any], context: Any  # pylint: disable=unused-argument
) -> Dict[str, Any]:
    """
    AWS Lambda handler function.

    Args:
        event: The event dict containing the request data
        context: The Lambda context object

    Returns:
        A dict containing the response with statusCode and body
    """
    print(f"Received event: {event}")

    return {
        "statusCode": 200,
        "body": "Hello from GitHub Actions Demo Lambda!",
        "headers": {"Content-Type": "application/json"},
    }
