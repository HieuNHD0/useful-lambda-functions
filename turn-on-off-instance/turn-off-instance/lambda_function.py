import boto3

instances_id = [''] # input your instance ID here
region = '' # input your AWS region here

def turn_off(event, context):
    
    client = boto3.client('ec2')
    stop_response = client.stop_instances(InstanceIds=instances_id)
    print('Stopped instance')