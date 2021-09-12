from boto3 import Session
import subprocess
import os
import sys
import pprint

from read_infra import readEC2
from write_infra import createEC2

TEMPLATE_PATH="./templates"

INPUT="input"
TARGET="target"
DEPLOYMENTS = {
    INPUT: None,
    TARGET: None
}

class Deployment:
    def __init__(self, profile_type):
        self.profile = input("Enter profile name of " + profile_type + " AWS deployment: ")
        self.region = input("Enter region of " + profile_type + " AWS deployment: ")
        os.environ['AWS_DEFAULT_REGION'] = self.region

    def set_access_key (self, access_key):
        self.access_key = access_key

    def set_secret_key (self, secret_key):
        self.secret_key = secret_key


def get_credentials(deployment_type):
    DEPLOYMENTS[deployment_type] = Deployment(deployment_type)
    try:
        session = Session(profile_name=DEPLOYMENTS[deployment_type].profile)
        credentials = session.get_credentials()
        # Credentials are refreshable, so accessing your access key / secret key
        # separately can lead to a race condition. Use this to get an actual matched
        # set.
        credentials = credentials.get_frozen_credentials()
        DEPLOYMENTS[deployment_type].set_access_key(credentials.access_key)
        DEPLOYMENTS[deployment_type].set_secret_key(credentials.secret_key)

    except:
        sys.exit("Error: invalid " + deployment_type + " profile.")

    if not DEPLOYMENTS[deployment_type].region:
        sys.exit("Error: invalid " + deployment_type + " region.")


if __name__ == "__main__":
    for deployment_type in DEPLOYMENTS.keys():
        get_credentials(deployment_type)
        # I would not recommend actually printing these. Generally unsafe.
        print(deployment_type + " profile access key: " + DEPLOYMENTS[deployment_type].access_key)
        print(deployment_type + " profile secret key: " + DEPLOYMENTS[deployment_type].secret_key)
        print(deployment_type + " profile region: " + DEPLOYMENTS[deployment_type].region)

    ec2_description = readEC2.read_EC2(DEPLOYMENTS[INPUT])
    ec2_reservations = ec2_description['Reservations']
    num_reservations = len(ec2_reservations)
    ec2_groups = []
    ec2_instances = []
    num_instances = 0
    # breakpoint()

    for idx in range(num_reservations):
        ec2_groups.append(ec2_reservations[idx]['Groups'])
        ec2_instances.append(ec2_reservations[idx]['Instances'])

    num_instances = len(ec2_instances)

    print ("No of EC2 instance reservations found: " + str(num_instances))
    print ("=================================================")
    pp = pprint.PrettyPrinter(indent=2)
    for instance in ec2_instances:
        pp.pprint(instance)
        print("=================================================")

