#!/bin/bash
aws ec2 authorize-security-group-ingress --group-id sg-01180c5c5f5e5f47e --protocol tcp --port 22 --cidr 0.0.0.0/0