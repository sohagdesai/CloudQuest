#!/bin/bash
aws ec2 create-security-group --group-name SSHAccess --description "Security group for SSH access" --vpc-id vpc-070aa2775f0e96e58