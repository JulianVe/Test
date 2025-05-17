import logging
import json
from message_provider_db import MessageProvider

message_provider = MessageProvider()

def handler(event, context):
    logging.info(f'handler {event} {context}')

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"text": message_provider.get_message()})
    }
