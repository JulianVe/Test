from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_iam as iam  # Import IAM for custom permissions

class LambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, dynamodb_table, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.lambda_function = _lambda.Function(
            self, "LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("../backend"),
            environment={"TABLE_NAME": dynamodb_table.table_name}
        )

        # ✅ Explicitly grant Scan permission
        self.lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Scan"],  # Ensure Scan is allowed
                resources=[dynamodb_table.table_arn]  # Apply to this table only
            )
        )
