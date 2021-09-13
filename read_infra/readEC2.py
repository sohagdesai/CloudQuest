import boto3

def read_ec2(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_instances()
    return response
