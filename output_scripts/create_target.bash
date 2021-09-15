aws ec2 create-vpc --cidr-block $CIDR_BLOCK --query Vpc.VpcId --output text --profile output --region us-west-1
aws ec2 create-subnet --vpc-id $VPC --cidr-block $CIDR
aws ec2 modify-subnet-attribute --subnet-id $SUBNET --map-public-ip-on-launch --profile output --region us-west-1
aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text
aws ec2 attach-internet-gateway --vpc-id $VPC --internet-gateway-id $GATEWAY --profile output --region us-west-1
aws ec2 create-route-table --vpc-id $VPC --query RouteTable.RouteTableId --output text --profile output --region us-west-1
aws ec2 create-route --route-table-id $ROUTE_TABLE --destination-cidr-block $CIDR_BLOCK --gateway-id $GATEWAY  --profile output --region us-west-1
aws ec2 associate-route-table --subnet-id $SUBNET --route-table-id $ROUTETABLE --profile output --region us-west-1
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
aws ec2 create-security-group --group-name $GROUP_NAME --description $DESCRIPTION --vpc-id $VPC --profile output --region us-west-1
aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP --protocol tcp --port $PORT --cidr $CIDR --profile output --region us-west-1
aws ec2 copy-image --source-image-id $SOURCE_IMAGE --source-region $SOURCE_REGION --profile output --region us-west-1 --name $NAME
aws ec2 run-instances --image-id ami-087c17d1fe0178315 --count 1 --instance-type t2.micro --security-group-ids sg-00021b160a0211adf --vpc-id vpc-7ed26403_ID --profile output --region us-west-1
aws ec2 create-vpc --cidr-block $CIDR_BLOCK --query Vpc.VpcId --output text --profile output --region us-west-1
aws ec2 create-subnet --vpc-id $VPC --cidr-block $CIDR
aws ec2 modify-subnet-attribute --subnet-id $SUBNET --map-public-ip-on-launch --profile output --region us-west-1
aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text
aws ec2 attach-internet-gateway --vpc-id $VPC --internet-gateway-id $GATEWAY --profile output --region us-west-1
aws ec2 create-route-table --vpc-id $VPC --query RouteTable.RouteTableId --output text --profile output --region us-west-1
aws ec2 create-route --route-table-id $ROUTE_TABLE --destination-cidr-block $CIDR_BLOCK --gateway-id $GATEWAY  --profile output --region us-west-1
aws ec2 associate-route-table --subnet-id $SUBNET --route-table-id $ROUTETABLE --profile output --region us-west-1
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
aws ec2 create-security-group --group-name $GROUP_NAME --description $DESCRIPTION --vpc-id $VPC --profile output --region us-west-1
aws ec2 authorize-security-group-ingress --group-id $SECURITY_GROUP --protocol tcp --port $PORT --cidr $CIDR --profile output --region us-west-1
aws ec2 copy-image --source-image-id $SOURCE_IMAGE --source-region $SOURCE_REGION --profile output --region us-west-1 --name $NAME
aws ec2 run-instances --image-id ami-087c17d1fe0178315 --count 1 --instance-type t2.micro --security-group-ids sg-00021b160a0211adf --vpc-id vpc-7ed26403_ID --profile output --region us-west-1
