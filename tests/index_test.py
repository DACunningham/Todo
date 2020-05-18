import json
import datetime
from src.index import handler


def test_index_handler():

    # Arrange
    event = {"body": '{"message": "hello.py--hello.handler Called"}'}
    data = {
        "output": event["body"],
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    context = {}

    expected = {
        "statusCode": 200,
        "body": json.dumps(data),
        "headers": {"Content-Type": "application/json"},
    }

    # Act
    result = handler(event, context)

    # Arrange
    assert result == expected
