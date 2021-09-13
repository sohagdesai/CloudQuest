import boto3

def read_route_table(creds):
    client = boto3.client(
        'route_table',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    response = client.describe_route_table()
    return response
