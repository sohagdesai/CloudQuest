import boto3

class RouteTable:
    description = {}
    def __init__(self, description):
        self.description = description

def get_route_tables(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    description = client.describe_route_tables()
    route_tables = RouteTable(description)
    return route_tables
