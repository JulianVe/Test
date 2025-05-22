from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_apigateway as apigateway

class APIStack(Stack):
    def __init__(self, scope: Construct, id: str, lambda_function, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.api = apigateway.RestApi(
            self, "APIGateway",
            rest_api_name="veasy_org_test_arq_message_api",
            deploy=False,
            description="Handles message retrieval.",
            default_cors_preflight_options={
                "allow_origins": apigateway.Cors.ALL_ORIGINS,
                "allow_methods": apigateway.Cors.ALL_METHODS,
                "allow_headers": ["Content-Type", "X-Amz-Date", "Authorization", "X-Api-Key", "X-Amz-Security-Token"]
            }
        )

        deployment = apigateway.Deployment(self, "Deployment", api=self.api)

        # Define a Usage Plan and associate it with "prod" stage
        usage_plan = self.api.add_usage_plan(
            "UsagePlan",
            name="BasicUsagePlan",
            throttle=apigateway.ThrottleSettings(
                rate_limit=5,  # Requests per second
                burst_limit=10  # Temporary burst limit
            )
        )

        prod_stage = apigateway.Stage(
            self, "ProdStage",
            deployment=deployment,
            stage_name="prod"
        )

        usage_plan.add_api_stage(stage=prod_stage)

        # Create API resource (/message)
        message_resource = self.api.root.add_resource("message")

        # Enable CORS for the /message resource
        message_resource.add_method(
            "GET",
            apigateway.LambdaIntegration(lambda_function)
        )
