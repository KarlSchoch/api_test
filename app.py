# Tutorial
# https://towardsdatascience.com/aws-lambda-with-custom-docker-images-as-runtime-9645b7baeb6f

import json

def handler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response