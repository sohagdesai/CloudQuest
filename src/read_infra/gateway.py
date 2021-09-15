import boto3
class Gateway:
    description = {}
    def __init__(self, description):
        self.description = description

def get_gateways(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_internet_gateways()
    gateways = Gateway(response)
    return gateways