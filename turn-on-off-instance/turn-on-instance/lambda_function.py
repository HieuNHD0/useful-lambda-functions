import boto3

instances_id = [''] # input your instance ID here
region = '' # input your AWS region here

def turn_on(event, context):
    
    client = boto3.client('ec2')
    start_response = client.start_instances(InstanceIds=instances_id)
    print('Started instance')