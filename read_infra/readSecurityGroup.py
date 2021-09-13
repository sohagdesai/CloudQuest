import boto3

def read_security_group(creds):
    client = boto3.client(
        'security_group',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_security_group()
    return response
