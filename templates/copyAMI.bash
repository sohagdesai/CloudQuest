#!/bin/bash
SOURCE_AMI=$1
SOURCE_REGION=$2
PROFILE=$3
REGION=$4
NAME=$5
aws ec2 copy-image --source-image-id $1 --source-region $2 --profile $3 --region $4 --name $5
