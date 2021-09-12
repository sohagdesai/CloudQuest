#!/bin/bash
aws ec2 associate-route-table --subnet-id $SUBNET --route-table-id $ROUTETABLE
