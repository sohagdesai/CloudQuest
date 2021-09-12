#!/bin/bash
aws ec2 run-instances --image-id $AMI --count $COUNT --instance-type $INSTANCE_TYPE --security-group-ids $SECURITY_GROUP --vpc-id $VPC_ID --profile $PROFILE --region REGION