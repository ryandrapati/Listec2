import boto3
import sys

region = sys.argv[1]
access_key = sys.argv[2]
secret_key = sys.argv[3]

client = boto3.client('ec2',
            region_name = region,
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key)
ec2Instances = client.describe_instances()

for reservation in ec2Instances['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            print (instance['InstanceId'])
            print(instance['InstanceType'])
            print(instance['State']['Name'])
            print(tag['Value'])
