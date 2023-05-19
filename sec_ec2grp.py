import boto3

ec2 = boto3.client('ec2')
instance_list = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

instance_id_list = []
security_grp = []
global security_grp_id
global subnet_ID
global vpc_id
global cidr_block
global availability_d
global nacl_id
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
            security_grp_id = sg['GroupId']
            get_rules(security_grp_id)

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

def subnet(subnet_id):
    subnet_array = ec2.describe_subnets(SubnetIds = subnet_id)
    subnet = subnet_array['Subnets'][0] 
    print('Subnet ID: {}'.format(subnet['SubnetId']))
    print('VPC ID: {}'.format(subnet['VpcId']))
    print('CIDR Block: {}'.format(subnet['CidrBlock']))
    print('Availability Zone: {}'.format(subnet['AvailabilityZone']))
    print('Network ACL ID: {}'.format(subnet['NetworkAclId']))

"""
def get_sg_grps(subnet_id):
   sub_list = ec2.describe_network_interfaces(
       Filters = [
            {
                'Name': 'subnet'
                'Values': [subnet_id]
            }            
        ]
    )
    sec_grps = []
    for interface in sub_list['NetworkInterfaces']:
        for security_group in interface['Groups']:
            sec_grps.append(security_group['GroupId'])
    print(sec_grps)
"""


#function to find subnets under vpc
def find_subnets(vpc_id):
    response = ec2.describe_subnets(
       Filters=[
           'Name': 'vpc_id',
           'Values': [vpc_id]
       ] 
    )
    subnet_ids_in_vpc = []
    for subnet in response['Subnets']:
        subnet_ids_in_vpc.append(subnet['SubnetId'])