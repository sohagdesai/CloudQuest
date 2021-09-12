#!/bin/bash
aws ec2 create-vpc --cidr-block $CIDR_BLOCK --query Vpc.VpcId --output text --profile $PROFILE --region $REGION
