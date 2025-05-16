import os
import boto3
import logging

MESSAGE_TABLE = os.getenv('DYNAMODB_TABLE', 'Messages')
REGION_NAME = os.getenv('AWS_REGION', 'eu-west-2')  # Default to eu-west-2

dynamodb = boto3.resource('dynamodb', region_name = REGION_NAME)
table = dynamodb.Table(MESSAGE_TABLE)

class MessageProvider:
    def get_message(self):
        logging.info('get_message')

        response = table.scan()
        items = response.get('Items', [])

        is_configured = items and len(items) > 0 and items[0]
        if not is_configured:
            logging.warning('no message configured')

        return items[0] if is_configured else "dynamic string"