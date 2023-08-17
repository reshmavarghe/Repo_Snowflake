import aws_cdk as core
import aws_cdk.assertions as assertions

from reshmas3snow.reshmas3snow_stack import Reshmas3SnowStack

# example tests. To run these tests, uncomment this file along with the example
# resource in reshmas3snow/reshmas3snow_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Reshmas3SnowStack(app, "reshmas3snow")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
