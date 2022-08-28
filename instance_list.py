import boto3
ec2 = boto3.client('ec2')
#for instance in ec2.instances.all():
#    print(
#         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
#         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
#         )
#     )

response = ec2.describe_instances()
print (response)