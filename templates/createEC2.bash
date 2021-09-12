#!/bin/bash
AMI=$1
COUNT=$2
INSTANCE_TYPE=$3
SECURITY_GROUP=$4
VPC_ID=$5
PROFILE=$6
REGION=$7
aws ec2 run-instances --image-id $1 --count $2 --instance-type $3 --security-group-ids $4 --vpc-id $5 --profile $6 --region $7
