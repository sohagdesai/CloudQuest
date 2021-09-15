# Overview
This program reverse engineers an AWS deployment and re-creates it in a target environment. The target can be in a different AWS account. 

# Approach
The approach taken is the following: 

1. The program takes as input: 
    - profile of the existing deployment to be reverse engineered
    - profile of the new deployment
   
   These profiles consists of:
   
   - access key
   - secret key
   - region
   
2. Based on the profile of the existing deployment, the program uses the Python `boto3` SDK to read the following low-level AWS entities and store them into in-memory data structures: 
	- EC2 instances
	- VPCs
	- KeyPairs
	- Internet Gateways
	- Subnets 
	- Routing Tables
	- Routes
	- Images used
	- Security Groups used
	
3. It then extracts parameters from the information it reads from Step 2, and modifies script templates implementing AWS CLI commands stored in the `write_infra/scriptTemplates` file, to construct output scripts that recreate the deployment using the profile of the new (target) deployment.

4. The order in which the AWS entities have to be created is critical. The following order has to be used:
   1. For each VPC identified in step 2, a VPC is created based on the associated CIDR block.  

   2. Using the VPC IDs from the previous step, a subnet is created for each CIDR block. 

   3. Internet Gateways are created.

   4. Using the IDs from the previous step, the internet gateways are attached to the VPCs. 

   5. A custom route table is created for each VPC.

   6. A route in the route table that points all traffic (0.0.0.0/0) to the internet gateway is created.

   7. Custom route tables are created and associated.

   8. A key pair is created with the same name as the key pair in the source deployment.

   9. Security groups are created per VPC.

   10. Rules are added to each security group. 
   
   11. Images for each EC2 instance are copied into the region for the new deployment.
    
   12. EC2 instances are then launched into the subnet, using: 
       - security group created
       - key pair created
       - image copied

       
   _Note_: The `--query` option is used for each command whose output is a dependency for the following command. 
   
# Structure
The following is the directory structure:
`$ ls -R README.md docs/ json/ output_scripts/ script_templates/ src/`

`README.md`

`docs/:`
`AWS_CLI_Create_Commands.txt`
`AWS_CLI_Delete_Commands.txt`

`json/:`
`DescribeInternetGateway.json  DescribeRouteTables.json      DescribeSubnets.json
DescribeNACLS.json            DescribeSecurityGroup.json    DescribeVPC.json`

`output_scripts/:
create_target.bash`

`script_templates/:
attachInternetGateway.bash     createInternetGateway.bash     createSecurityGroup.bash       modifySubnetAttribute.bash
attachRouteTable.bash          createKeyPair.bash             createSecurityGroupRules.bash
copyImage.bash                 createRoute.bash               createSubnet.bash
createEC2.bash                 createRouteTable.bash          createVPC.bash
`
`src/:
main.py      read_infra/  tests/       utils/       write_infra/
`
`src/read_infra:
__init__.py       ec2.py            image.py          route.py          securityGroup.py  vpc.py
     gateway.py        keyPair.py        routeTable.py     subnet.py`

`src/tests:
__init__.py    readTests.py   writeTests.py
`
`src/utils:
__init__.py      credential.py
`

`src/write_infra:
__init__.py                createScripts.py    scriptTemplates.py`



# Running the Program
1. Run: `python3 main.py`
   - provide the input profile, the input region, target profile, target region

2. Run: `output_scripts/create_target.bash`
