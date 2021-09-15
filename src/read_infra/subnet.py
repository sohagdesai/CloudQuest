import boto3
class Subnet:
    description = {}
    def __init__(self, description):
        self.description = description

def get_subnets(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    description = client.describe_subnets()
    subnets = Subnet(description)
    return subnets
