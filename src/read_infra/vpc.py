import boto3

class VPC:
    vpcs = []
    def __init__(self, vpcs):
        self.vpcs.append(vpcs)

def get_vpcs(creds):
    ec2 = boto3.resource('ec2', region_name=creds.region)
    filters = [{}]
    vpc_ids = VPC(list(ec2.vpcs.filter(Filters=filters)))
    return vpc_ids