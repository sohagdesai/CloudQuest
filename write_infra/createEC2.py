import subprocess
import sys

def createEC2(ec2_create_script_path,image,count,instance_type,security_group_id,vpc_id,profile,region):
   try:
       subprocess.check_call([
           ec2_create_script_path,
           image,
           count,
           instance_type,
           security_group_id,
           vpc_id,
           profile,
           region
       ])
   except:
       sys.exit("Error: could not run EC2 create bash script.")
