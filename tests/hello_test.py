import json
from src.hello import handler


def test_hello_handler():

    # Arrange
    event = {"body": '{"message": "hello.py--hello.handler Called"}'}
    context = {}

    expected = {
        "statusCode": 200,
        "body": json.dumps(event["body"]),
        "headers": {"Content-Type": "application/json"},
    }

    # Act
    result = handler(event, context)

    # Arrange
    assert result == expected
