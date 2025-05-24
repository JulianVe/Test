from aws_cdk import App

from stacks.dynamodb_stack import DynamoDBStack
from stacks.lambda_stack import LambdaStack
from stacks.api_stack import APIStack
from stacks.s3_stack import S3Stack

app = App()

stack_prefix = "TestArq"

dynamodb_stack = DynamoDBStack(app, stack_prefix + "DynamoDBStack")
lambda_stack = LambdaStack(app, stack_prefix + "LambdaStack", dynamodb_table=dynamodb_stack.table)
api_stack = APIStack(app, stack_prefix + "APIStack", lambda_function=lambda_stack.lambda_function)
s3_stack = S3Stack(app, stack_prefix + "S3Stack")

app.synth()
