from aws_cdk import (
    # Duration,
    App,
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
)
from constructs import Construct

class Reshmas3SnowStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            id="reshmasnows3bucket",
            bucket_name="reshmasnows3bucket",
            encryption=s3.BucketEncryption.KMS,
            bucket_key_enabled=True
                )
        result1 = bucket.add_to_resource_policy
        (
            iam.PolicyStatement(
            actions=["s3:*", "ec2:*"],
            resources=[bucket.arn_for_objects("*")],
            principals=[iam.AccountRootPrincipal()]
            )
        )
        role = iam.Role(self, "RVRole",
            assumed_by = iam.ServicePrincipal("s3.amazonaws.com"),
            description="Example role for s3"
        )
        role.add_to_policy(iam.PolicyStatement(
        resources=["*"],
        actions=["lambda:*"]
))
