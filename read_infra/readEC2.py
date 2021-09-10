import boto3
import pprint

def read_EC2(profile):
    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=profile.access_key,
        aws_secret_access_key=profile.secret_key,
        region_name = profile.region
    )
    response = ec2_client.describe_instances()
    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(response)
    return response