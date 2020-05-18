import json
from src.hello import handler


def test_hello_handler():

    # Arrange
    event = {"pathParameters": {"name": "Dexter-testname"}}
    context = {}

    expected = {
        "statusCode": 200,
        "body": '{"output": "Hello Dexter-testname"}',
        "headers": {"Content-Type": "application/json"},
    }

    # Act
    result = handler(event, context)

    # Arrange
    assert result == expected
