import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError

def lambda_handler(event, context):
    #Debugging local issues
    print(os.environ)
    # Create a DynamoDB resource
    if 'development' == 'development':
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        dynamodb = boto3.resource('dynamodb')
        
        
    table = dynamodb.Table('cloud9_table')

    try:
        response = table.put_item(
            Item={
                'id': event['id'],
                'name': event['name'],
                # Add as many attributes as you want
            }
        )
        return {
            'statusCode': 200,
            'body': 'Item added!'
        }
    except BotoCoreError as e:
        return {
            'statusCode': 400,
            'body': 'Error adding item: {}'.format(e.response['Error']['Message'])
        }
