
import boto3
import os

def upload_audio_to_s3(file_path, aws_access_key_id, aws_secret_access_key, aws_region_name, s3_bucket_name):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name
    )

    s3 = session.resource('s3')

    file_name = os.path.basename(file_path)
    s3_object = s3.Object(s3_bucket_name, file_name)
    s3_object.upload_file(file_path)

    return s3_object.key

def upload_video_to_s3(file_path, aws_access_key_id, aws_secret_access_key, aws_region_name, s3_bucket_name):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name
    )

    s3 = session.resource('s3')

    file_name = os.path.basename(file_path)
    s3_object = s3.Object(s3_bucket_name, file_name)
    s3_object.upload_file(file_path)

    return s3_object.key


#function to access stuff from s3 and store it in dynamodb
def download_from_s3(bucket_name, object_key, file_path,database, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, aws_region_name=None):
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name,
        aws_session_token=aws_session_token
    )
    s3=session.resource('s3')
    s3_object = s3.Object(bucket_name, object_key)
    s3_object.download_file(file_path)
    
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(database)
    table.put_item(Item={
        'Bucket': bucket_name,
        'Key': object_key,
        'Path': file_path
    })






#from s3_upload_module import upload_file_to_s3

#aws_access_key_id = 'acees key'
#aws_secret_access_key = 'secret key'
#aws_region_name = 'region name'
#s3_bucket_name = 'bucket'

#file_path = 'path'

#upload_file_to_s3(file_path, aws_access_key_id, aws_secret_access_key, aws_region_name, s3_bucket_name):
