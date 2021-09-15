import boto3
class SecurityGroup:
    description = {}
    def __init__(self, description):
        self.description = description

def get_security_groups(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    description = client.describe_security_groups()
    security_groups = SecurityGroup(description)
    return security_groups
