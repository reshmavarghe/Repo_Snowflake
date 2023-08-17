from aws_cdk import (
    # Duration,
    App,
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class Reshmas3SnowStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Reshmas3SnowQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        s3.Bucket(
            self,
            id="reshmasnows3bucket",
            bucket_name="reshmasnows3bucket",
            encyption=s3.BucketEncryption.KMS,
            bucket_key_enabled=True
                )
