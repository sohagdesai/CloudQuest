#!/bin/bash
aws ec2 create-route --route-table-id $ROUTE_TABLE --destination-cidr-block $CIDR_BLOCK --gateway-id $GATEWAY  --profile $PROFILE --region $REGION
