import json
import datetime
from src.index import handler


def test_index_handler():

    # Arrange
    event = {"body": {"message": "index.py--index.handler Called"}}
    data = {
        "output": event["body"],
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    context = {}

    expected = {
        "statusCode": 200,
        "body": data,
        "headers": {"Content-Type": "application/json"},
    }

    # Act
    result = handler(event, context)
    dtg = json.loads(result["body"])
    expected["body"]["timestamp"] = dtg["timestamp"]
    expected["body"] = json.dumps(expected["body"])

    # Arrange
    assert result == expected
