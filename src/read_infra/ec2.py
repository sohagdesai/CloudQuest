import boto3

class EC2:
    groups = []
    instances = []
    instance_types = []
    images = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description
        self.reservations = self.description["Reservations"]
        self.num_reservations = len(self.description["Reservations"])
        #breakpoint()
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])
            self.instances.append(self.reservations[idx]['Instances'])
            self.num_instances += len(self.reservations[idx]['Instances'])
            for idx2 in range(len(self.reservations[idx]['Instances'])):
                self.images.append(self.reservations[idx]['Instances'][idx2]['ImageId'])
        for instance in self.instances:
            self.instance_types.append(instance[0]["InstanceType"])

def get_ec2_instances(creds):
    client = boto3.client(
        'ec2',
        aws_access_key_id=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        region_name = creds.region
    )
    description = client.describe_instances()
    ec2_instances = EC2(description)
    return ec2_instances
