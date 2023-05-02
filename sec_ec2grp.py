import boto3

ec2 = boto3.client('ec2')
instance_list = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

instance_id_list = []
security_grp = []
for res in instance_list['Reservations']:
    for instance in res['Instances']:
        instance_id_list.append(instance['Instanceid'])
        for group in instance['SecurityGroups']:
            security_grp.append(group['GroupId'])

def match(input_id):
    for input_id in instance_id_list:
        response = ec2.describe_instances(InstanceIds=[input_id])
        security_groups = response['Reservations'][0]['Instances'][0]['SecurityGroups']
        for sg in security_groups:
            print('Security Group ID: {}\nSecurity Group Name: {}'.format(sg['GroupId'], sg['GroupName']))
            get_rules(sg['GroupId'])

def get_rules(sg_id):
    sg_array = ec2.describe_security_groups(GroupIds=[sg_id])
    inbound_rules = sg_array['SecurityGroups'][0]['IpPermissions']
    outbound_rules = sg_array['SecurityGroups'][0]['IpPermissionsEgress']
    print('Inbound Rules:')
    for rule in inbound_rules:
        print(rule)

    print ('Outbound Rules:')
    for rule in outbound_rules:
        print(rule)