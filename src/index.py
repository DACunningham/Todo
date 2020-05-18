import json
import datetime


def handler(event, context):
    data = {
        "output": event["body"],
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }
    return {
        "statusCode": 200,
        "body": data,
        "headers": {"Content-Type": "application/json"},
    }
