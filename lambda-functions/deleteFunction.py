import json
import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError

def lambda_handler(event, context):
    # Retrieve the item ID from the event
    item_id = event['pathParameters']['id']
    
    # Create a DynamoDB resource
    if os.environ['ENV'] == 'development':
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        dynamodb = boto3.resource('dynamodb')
        
    # Get the DynamoDB table
    table = dynamodb.Table('cloud9_table')
    
    try:
        # Delete the item from DynamoDB
        response = table.delete_item(
            Key={
                'id': item_id
            }
        )
        
        # Return a success response
        return {
            'statusCode': 200,
            'body': 'Item deleted successfully'
        }
    
    except BotoCoreError as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': 'Error deleting item: {}'.format(str(e))
        }
