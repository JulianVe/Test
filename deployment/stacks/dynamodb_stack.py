from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_dynamodb as dynamodb

TABLE_NAME = "VeasyOrgTestArqMessages"

class DynamoDBStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.table = dynamodb.Table(
            self, TABLE_NAME,
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )
