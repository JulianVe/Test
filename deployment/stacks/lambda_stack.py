from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_lambda as _lambda
from .dynamodb_stack import TABLE_NAME

class LambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, dynamodb_table, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.lambda_function = _lambda.Function(
            self, "veasy_org_test_arq_message_lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("../backend"),
            environment={TABLE_NAME: dynamodb_table.table_name}
        )

        dynamodb_table.grant_read_data(self.lambda_function)
