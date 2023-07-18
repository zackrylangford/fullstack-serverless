import json
import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError

def lambda_handler(event, context):
    # Retrieve the item ID from the event
    item_id = event['pathParameters']['id']
    
    # Create a DynamoDB resource
    if 'development' == 'development':
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        dynamodb = boto3.resource('dynamodb')
    
    # Get the DynamoDB table
    table = dynamodb.Table('cloud9_table')
    
    try:
        # Retrieve the item from DynamoDB
        response = table.get_item(
            Key={
                'id': item_id
            }
        )
        
        # Extract the item from the response
        item = response.get('Item')
        
        if item:
            # Return the item as the response
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            # Return a not found response
            return {
                'statusCode': 404,
                'body': 'Item not found'
            }
    
    except BotoCoreError as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': 'Error retrieving item: {}'.format(str(e))
        }
