#!/bin/bash
aws ec2 attach-internet-gateway --vpc-id $VPC --internet-gateway-id $GATEWAY --profile $PROFILE --region $REGION
