import logging
import json
from message_provider_static import MessageProvider

message_provider = MessageProvider()

def lambda_hander(event, context):
    logging.info('message')

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"text": message_provider.get_message()})
    }
