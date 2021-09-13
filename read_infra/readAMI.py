import boto3

def read_AMI(creds):
    client = boto3.client(
        'ami',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_ami()
    return response
