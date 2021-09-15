import boto3
class KeyPair:
    description = {}
    def __init__(self, description):
        self.description = description

def get_keypairs(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_key_pairs()
    keypairs = KeyPair(response)
    return keypairs