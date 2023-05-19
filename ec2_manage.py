import sys
import boto3
from botocore.exceptions import ClientError

ec2= boto3.client('ec2')

#list all running ec2 instances
region = "ap-southeast-2"

resource = boto3.resource('ec2', region)
state = 'running'
#fi = filtered instances

