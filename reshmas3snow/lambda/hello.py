import json

def lambda_handler(event, context):
    json.dumps(event)
    json.dumps(context)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello From S3')
    }