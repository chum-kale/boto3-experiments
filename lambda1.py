import boto3
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-dynamodb-table')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_size = record['s3']['object']['size']
        file_type = record['s3']['object']['contentType']
        file_last_modified = record['s3']['object']['lastModified']
        
        # Store metadata in DynamoDB
        response = table.put_item(
            Item={
                'bucket_name': bucket_name,
                'object_key': object_key,
                'file_size': file_size,
                'file_type': file_type,
                'file_last_modified': file_last_modified
            }
        )
        
        print(response)

    return {
        'statusCode': 200,
        'body': 'Metadata stored in DynamoDB'
    }
