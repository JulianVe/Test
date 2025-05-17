import os
import boto3
import logging

TABLE_NAME = "DynamoDBStack-VeasyOrgTestArqMessages88CC98E1-3R88WVBLN3AE"
REGION_NAME = 'eu-west-2'

dynamodb = boto3.resource('dynamodb', region_name = REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

class MessageProvider:
    def get_message(self):
        logging.info('get_message')

        response = table.scan()
        items = response.get('Items', [])

        is_configured = items and len(items) > 0 and items[0]
        if not is_configured:
            logging.warning('no message configured')

        return items[0] if is_configured else "dynamic string"