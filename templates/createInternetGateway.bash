#!/bin/bash
aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text