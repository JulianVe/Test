from aws_cdk import Stack, CfnOutput
from constructs import Construct
import aws_cdk.aws_s3 as s3

BUCKET_NAME = "veasy.org.test.arq"

class S3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create a new bucket.
        self.bucket = s3.Bucket(
            self, "FrontendBucket",
            bucket_name=BUCKET_NAME,
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
            public_read_access=True,
            website_index_document="index.html"
        )

        # Add CORS configuration. 
        self.bucket.add_cors_rule(
            allowed_methods=[s3.HttpMethods.GET, s3.HttpMethods.POST],
            allowed_origins=["*"],
            allowed_headers=["*"]
        )

        # Output the website URL of the bucket.
        CfnOutput(
            self, "BucketWebsiteURL",
            value=self.bucket.bucket_website_url
        )
