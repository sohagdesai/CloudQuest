import boto3
import sys
import pprint
from boto3 import Session

from read_infra import ec2
from read_infra import vpc
from read_infra import gateway
from read_infra import keyPair
from read_infra import routeTable
from read_infra import securityGroup
from read_infra import subnet
from read_infra import image
from read_infra import route


from utils import credential

if __name__ == "__main__":
    creds = credential.Credential ("input", "us-east-1")
    try:
        session = Session(profile_name="input")
        session_creds = session.get_credentials()
        # Credentials are refreshable, so accessing your access key / secret key
        # separately can lead to a race condition. Use this to get an actual matched
        # set.
        frozen_creds = session_creds.get_frozen_credentials()
        creds.set_access_key(frozen_creds.access_key)
        creds.set_secret_key(frozen_creds.secret_key)

    except:
        sys.exit("Error: invalid profile.")

    if not creds.region:
        sys.exit("Error: invalid region.")

    print ("==================EC2=====================")
    ec2_instances = ec2.get_ec2_instances(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(ec2_instances.description)

    print ("==================VPCs=====================")
    vpcs = vpc.get_vpcs(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(vpcs.vpcs)

    print ("================Gateways===================")
    gateways = gateway.get_gateways(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(gateways.description)

    print ("===============Key Pairs=====================")
    keypairs = keyPair.get_keypairs(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(keypairs.description)

    # print ("===============Route Tables==================")
    route_tables = routeTable.get_route_tables(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(route_tables.description)

    print ("===============Security Groups===============")
    security_groups = securityGroup.get_security_groups(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(security_groups.description)

    print ("==================Subnets====================")
    subnets = subnet.get_subnets(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(subnets.description)

    print ("==================Images=====================")
    images = image.get_images(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(images.images)

    print ("==================Routes=====================")
    routes = route.get_routes(creds)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(routes.routes)
