# Overview
This program reverse engineers an AWS deployment and re-creates it in a target environment. The target can be in a different AWS account. 

# Approach
The approach taken is the following: 

1. The program takes as input: 
    - profile of the existing deployment to be reverse engineered
    - profile of the new deployment
   
   These profile consists of:
   
   - access key
   - secret key
   - region
   
2. Based on the profile of the existing deployment the program uses the Python `boto3` SDK to read the following low-level AWS entities and store them into in-memory data structures: 
	- EC2 instances
	- VPCs
	- KeyPairs
	- Internet Gateways
	- Subnets 
	- Routing Tables
	- Routes
	- AMIs used
	- Security Groups
	
3. It then extracts parameters from the information it reads from Step 2, and script templates implementing AWS CLI commands stored in the `script_templates` directory, to construct scripts that recreate the deployment using the profile of the new deployment.

4. The order in which the AWS entities have to be created is critical. The following order has to be used:
   1. For each VPC identified in step 2, VPC is created based on the associated CIDR block.  

   2. Using the VPC IDs from the previous step, a subnet is created for each CIDR block 

   3. Internet Gateways are created.

   4. Using the ID from the previous step, the internet gateways are attached to the VPCs. 

   5. A custom route table is created for each VPC

   6. A route in the route table that points all traffic (0.0.0.0/0) to the internet gateway is created.

   7. Custom route tables are created and associated.

   8. A key pair is created.

   9. A security group is created in each VPC

   10. Rules are added to each security group. 
   
   11. AMI is copied into the region for the new deplyment.
    
   12. EC2 instances are then launched into the subnet, using: 
       - security group created
       - key pair created. 
       - AMI copied

       
   _Note_: The `--query` option is used for each command whose output is a dependency for the following command. 
   
# Structure
The following is the directory structure:

`README.md      cloudQuest.py`

`docs/:
AWS_CLI_Create_Commands.txt  AWS_CLI_Delete_Commands.txt`

`json/:
DescribeInternetGateway.json  DescribeRouteTables.json      DescribeSubnets.json
DescribeNACLS.json            DescribeSecurityGroup.json    DescribeVPC.json`

`output_scripts/:
recreateDeployment.bash
`

`read_infra/:
__init__.py           readAMI.py            readGateway.py        readRoute.py          readSecurityGroup.py  readVPC.py
readEC2.py            readKeyPair.py        readRouteTable.py     readSubnet.py
`

`script_templates/:
attachInternetGateway.bash     createEC2.bash                 createRoute.bash               createSecurityGroupRules.bash
attachRouteTable.bash          createInternetGateway.bash     createRouteTable.bash          createVPC.bash
copyAMI.bash                   createKeyPair.bash             createSecurityGroup.bash       modifySubnetAttribute.bash`

`write_infra/:
__init__.py   attachInternetGateway.py     createEC2.py                createRoute.py               createSecurityGroupRules.py
attachRouteTable.py          createInternetGateway.py     createRouteTable.py          createVPC.py
copyAMI.py                   createKeyPair.py             createSecurityGroup.py       modifySubnetAttribute.py`


# Running the Program
1. Run: `python3 cloudQuest`
   - provide the input profile, the input region, target profile, target region

2. Run: `output_scripts/recreateDeployment.bash`
