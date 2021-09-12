#!/bin/bash
aws ec2 create-route-table --vpc-id vpc-070aa2775f0e96e58 --query RouteTable.RouteTableId --output text