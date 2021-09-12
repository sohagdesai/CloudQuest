#!/bin/bash
aws ec2 create-route --route-table-id rtb-040f187195beb8511 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-0db795865df3816b4