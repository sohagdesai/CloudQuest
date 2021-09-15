#!/bin/bash
aws ec2 copy-image --source-image-id $SOURCE_AMI --source-region $SOURCE_REGION --profile $PROFILE --region $REGION --name $NAME
