from utils import credential
from read_infra import ec2
from read_infra import vpc
from read_infra import gateway
from read_infra import keyPair
from read_infra import routeTable
from read_infra import securityGroup
from read_infra import subnet
from read_infra import image
from read_infra import route

from write_infra import createScripts

OUTPUT_PATH="/Users/sohag/PGPCC/CloudQuest/output_scripts/"

INPUT="input"
TARGET="target"

def get_deployment_info(deployment, profile_type):
    creds                        = credential.get_credentials(profile_type)
    deployment["credentials"]    = creds
    deployment["profile"]        = creds.profile
    deployment["region"]         = creds.region
    deployment["profile_type"]    = profile_type
    deployment["ec2"]            = ec2.get_ec2_instances(creds)
    deployment["vpc"]            = vpc.get_vpcs(creds)
    deployment["gateway"]        = gateway.get_gateways(creds)
    deployment["keypair"]        = keyPair.get_keypairs(creds)
    deployment["image"]          = image.get_images(creds)
    deployment["route_table"]    = routeTable.get_route_tables(creds)
    deployment["security_group"] = securityGroup.get_security_groups(creds)
    deployment["subnet"]         = subnet.get_subnets(creds)
    deployment["route"]          = route.get_routes(creds)

    return deployment

def recreate_deployment(deployment, profile_type):
    creds                        = credential.get_credentials(profile_type)
    output_script_dict = createScripts.create_output_scripts (deployment, creds)
    output_script_list = []
    for k in output_script_dict.keys():
        output_script_list.append(output_script_dict[k])

    createScripts.write_output_scripts(output_script_list, profile_type, OUTPUT_PATH)

if __name__ == "__main__":
    input_deployment = {}
    input_deployment = get_deployment_info(input_deployment, INPUT)
    recreate_deployment(input_deployment, TARGET)
