from boto3 import Session
import subprocess
import os
import sys
import pprint

from read_infra import readEC2
from read_infra import readAMI
from read_infra import readVPC
from read_infra import readGateway
from read_infra import readKeyPair
from read_infra import readRoute
from read_infra import readRouteTable
from read_infra import readSecurityGroup
from read_infra import readSubnet

from write_infra import createEC2

TEMPLATE_PATH="./script_templates"
OUTPUT_PATH="./output_scripts"

INPUT="input"
TARGET="target"

deployment = {
    "profile": None,
    "region": None,
    "credentials": None,
    "ami": None,
    "ec2": None,
    "keypair": None,
    "gateway": None,
    "vpc": None,
    "route_table": None,
    "route": None,
    "security_group": None,
    "subnet": None,
}

class Credential:
    def __init__(self, profile_type):
        self.profile = input("Enter profile name of " + profile_type + " AWS deployment: ")
        self.region = input("Enter region of " + profile_type + " AWS deployment: ")
        os.environ['AWS_DEFAULT_REGION'] = self.region

    def set_access_key (self, access_key):
        self.access_key = access_key

    def set_secret_key (self, secret_key):
        self.secret_key = secret_key

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class VPC:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class Gateway:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")

class EC2:
    groups = []
    instances = []
    description = {}
    num_reservations = 0
    num_instances = 0
    def __init__(self, description):
        self.description = description

    def get_reservations(self):
        self.reservations = self.description["reservations"]

    def get_groups(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.groups.append(self.reservations[idx]['Groups'])

    def get_instances(self):
        self.num_reservations = len(self.description["reservations"])
        for idx in range(self.num_reservations):
            self.instances.append(self.reservations[idx]['Instances'])

    def print_info(self):
        print("No of EC2 instance reservations found: " + str(self.num_instances))
        print("=================================================")
        pp = pprint.PrettyPrinter(indent=2)
        for instance in self.instances:
            pp.pprint(instance)
            print("=================================================")



def get_credentials(deployment_type):
    deployment["profile"] = deployment_type
    deployment["credentials"] = Credential(deployment_type)
    try:
        session = Session(profile_name=deployment["profile"])
        session_creds = session.get_credentials()
        # Credentials are refreshable, so accessing your access key / secret key
        # separately can lead to a race condition. Use this to get an actual matched
        # set.
        frozen_creds = session_creds.get_frozen_credentials()
        deployment["credentials"].set_access_key(frozen_creds.access_key)
        deployment["credentials"].set_secret_key(frozen_creds.secret_key)

    except:
        sys.exit("Error: invalid " + deployment_type + " profile.")

    if not deployment["credentials"].region:
        sys.exit("Error: invalid " + deployment_type + " region.")

def get_ec2_info(creds):
    description = readEC2.read_ec2(creds)
    deployment["ec2"] = EC2(description)

def get_vpc_info(creds):
    description = readVPC.read_vpc(creds)
    deployment["ec2"] = EC2[description]


def get_gateway_info(creds):
    description = readGateway.read_gateway(creds)
    deployment["ec2"] = EC2[description]


def get_keypair_info(creds):
    description = readKeyPair.read_keypair(creds)
    deployment["ec2"] = EC2[description]


def get_ami_info(creds):
    description = readAMI.read_ami(creds)
    deployment["ec2"] = EC2[description]


def get_route_table_info(creds):
    description = readRouteTable.read_route_table(creds)
    deployment["ec2"] = EC2[description]


def get_security_group_info(creds):
    description = readSecurityGroup.read_security_group(creds)
    deployment["ec2"] = EC2[description]


def get_subnet_info(creds):
    description = readSubnet.read_subnet(creds)
    deployment["ec2"] = EC2[description]


def get_route_info(creds):
    description = readRoute.read_route(creds)
    deployment["ec2"] = EC2[description]


def get_deployment_info(creds):
    deployment["ec2"]            = get_ec2_info(creds)
    deployment["vpc"]            = get_vpc_info(creds)
    deployment["gateway"]        = get_gateway_info(creds)
    deployment["keypair"]        = get_keypair_info(creds)
    deployment["ami"]            = get_ami_info(creds)
    deployment["route_table"]    = get_route_table_info(creds)
    deployment["security_group"] = get_security_group_info(creds)
    deployment["subnet"]         = get_subnet_info(creds)
    deployment["route"]          = get_route_info(creds)


if __name__ == "__main__":
    #breakpoint()
    get_credentials(INPUT)
    # I would not recommend actually printing these. Generally unsafe.
    # print(deployment_type + " profile access key: " + DEPLOYMENTS[deployment_type].access_key)
    # print(deployment_type + " profile secret key: " + DEPLOYMENTS[deployment_type].secret_key)
    # print(deployment_type + " profile region: " + DEPLOYMENTS[deployment_type].region)
    get_deployment_info(deployment["credentials"])
    breakpoint()