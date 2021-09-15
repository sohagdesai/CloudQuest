scripts = {
    "create_vpc": "aws ec2 create-vpc --cidr-block $CIDR_BLOCK --query Vpc.VpcId --output text --profile $PROFILE --region $REGION\n",
    "create_subnet": "aws ec2 create-subnet --vpc-id $VPC --cidr-block $CIDR\n",
    "modify_subnet_attribute": "aws ec2 modify-subnet-attribute --subnet-id $SUBNET --map-public-ip-on-launch --profile $PROFILE --region $REGION\n",
    "create_internet_gateway": "aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text\n",
    "attach_internet_gateway": "aws ec2 attach-internet-gateway --vpc-id $VPC --internet-gateway-id $GATEWAY --profile $PROFILE --region $REGION\n",
    "create_route_table": "aws ec2 create-route-table --vpc-id $VPC --query RouteTable.RouteTableId --output text --profile $PROFILE --region $REGION\n",
    "create_route": "aws ec2 create-route --route-table-id $ROUTE_TABLE --destination-cidr-block $CIDR_BLOCK --gateway-id $GATEWAY  --profile $PROFILE --region $REGION\n",
    "associate_route_table": "aws ec2 associate-route-table --subnet-id $SUBNET --route-table-id $ROUTETABLE --profile $PROFILE --region $REGION\n",
    "create_key_pair": "aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem\n",
    "create_security_group": "aws ec2 create-security-group --group-name $GROUP_NAME --description $DESCRIPTION --vpc-id $VPC --profile $PROFILE --region $REGION\n",
    "authorize_security_group_ingress": "aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP --protocol tcp --port $PORT --cidr $CIDR --profile $PROFILE --region $REGION\n",
    "copy_image": "aws ec2 copy-image --source-image-id $SOURCE_IMAGE --source-region $SOURCE_REGION --profile $PROFILE --region $REGION --name $NAME\n",
    "run_instances": "aws ec2 run-instances --image-id $IMAGE --count $COUNT --instance-type $INSTANCE_TYPE --security-group-ids $SECURITY_GROUP --vpc-id $VPC_ID --profile $PROFILE --region $REGION\n"
}