import boto3
from . import ec2

class Image:
    images = []
    def __init__(self, images):
        self.images = images


def get_images(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_instances()
    ec2_instances = ec2.EC2(response)
    images = Image(ec2_instances.images)
    return images