from aws_cdk import App

from stacks.dynamodb_stack import DynamoDBStack
from stacks.lambda_stack import LambdaStack
from stacks.api_stack import APIStack
from stacks.s3_stack import S3Stack

app = App()

dynamodb_stack = DynamoDBStack(app, "DynamoDBStack")
lambda_stack = LambdaStack(app, "LambdaStack", dynamodb_table=dynamodb_stack.table)
api_stack = APIStack(app, "APIStack", lambda_function=lambda_stack.lambda_function)
s3_stack = S3Stack(app, "S3Stack")

app.synth()
