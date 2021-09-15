from . import scriptTemplates


def replace_profile_and_region (script, profile, region):
    return script.replace("$PROFILE", profile).replace("$REGION", region)

def create_output_scripts(input_deployment, output_creds):
    output_profile = output_creds.profile
    output_region = output_creds.region

    for key in scriptTemplates.scripts.keys():
        scriptTemplates.scripts[key] = replace_profile_and_region(scriptTemplates.scripts[key], output_profile, output_region)

    #breakpoint()
    # scriptTemplates.scripts["create_vpc"] = scriptTemplates.scripts["create_vpc"].replace("$VPC", input_deployment["vpc"].vpcs[0][0].id)
    # scriptTemplates.scripts["create_vpc"] = scriptTemplates.scripts["create_vpc"].replace("$GATEWAY", input_deployment["gateway"].description)
    # scriptTemplates.scripts["create_subnet"] = scriptTemplates.scripts["create_subnet"].replace("$VPC", input_deployment["vpc"].vpcs[0])
    # scriptTemplates.scripts["create_gateway"] = scriptTemplates.scripts["create_gateway"]
    # scriptTemplates.scripts["create_route_table"] = scriptTemplates.scripts["create_route_table"]
    # scriptTemplates.scripts["create_route"] = scriptTemplates.scripts["create_route"].replace("$ROUTE_TABLE", input_deployment["route_table"].route_tables[0])
    # scriptTemplates.scripts["associate_route_table"] = scriptTemplates.scripts["associate_route_table"]
    # scriptTemplates.scripts["create_key_pair"] = scriptTemplates.scripts["create_key_pair"]
    # scriptTemplates.scripts["create_security_group"] = scriptTemplates.scripts["create_security_group"]
    # scriptTemplates.scripts["authorize_security_group_ingress"] = scriptTemplates.scripts["authorize_security_group_ingress"]
    # scriptTemplates.scripts["copy_image"] = scriptTemplates.scripts["copy_image"]
    scriptTemplates.scripts["run_instances"] = scriptTemplates.scripts["run_instances"].replace("$IMAGE", input_deployment["image"].images[0])
    scriptTemplates.scripts["run_instances"] = scriptTemplates.scripts["run_instances"].replace("$COUNT", "1")
    scriptTemplates.scripts["run_instances"] = scriptTemplates.scripts["run_instances"].replace("$INSTANCE_TYPE", input_deployment["ec2"].instance_types[0])
    scriptTemplates.scripts["run_instances"] = scriptTemplates.scripts["run_instances"].replace("$SECURITY_GROUP", input_deployment["security_group"].description["SecurityGroups"][0]["GroupId"])
    scriptTemplates.scripts["run_instances"] = scriptTemplates.scripts["run_instances"].replace("$VPC", input_deployment["vpc"].vpcs[0][0].id)
    return scriptTemplates.scripts

def write_output_scripts(scripts, profile_type, path):
    f = open(path + "create_" + profile_type + ".bash", "a")
    for script in scripts:
        f.writelines(script)
    f.close()
