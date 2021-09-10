import boto3
from boto3 import Session
import os.path
from os import path
import sys
import read_infra
import write_infra

if __name__ == "__main__":
    session = Session(profile_name='input')
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    credentials = session.get_credentials()
    # Credentials are refreshable, so accessing your access key / secret key
    # separately can lead to a race condition. Use this to get an actual matched
    # set.
    current_credentials = credentials.get_frozen_credentials()

    # I would not recommend actually printing these. Generally unsafe.
    print("Input profile access key: " + current_credentials.access_key)
    print("Input profile secret key: " + current_credentials.secret_key)
    print("Input profile region: " + session.region_name)

    session = Session(profile_name='output')
    os.environ['AWS_DEFAULT_REGION'] = 'us-west-1'
    credentials = session.get_credentials()
    # Credentials are refreshable, so accessing your access key / secret key
    # separately can lead to a race condition. Use this to get an actual matched
    # set.
    current_credentials = credentials.get_frozen_credentials()

    # I would not recommend actually printing these. Generally unsafe.
    print("Output profile access key: " + current_credentials.access_key)
    print("Output profile secret key: " + current_credentials.secret_key)
    print("Output profile region: " + session.region_name)


    # session = botocore.session.get_session()
    # print(session.get_credentials().access_key)
    # print(session.get_credentials().secret_key)
    # input_path  = input("Enter pathname of source AWS deployment: ")
    # if not path.exists(input_path):
    #    sys.exit ("Error: invalid pathname for input credentials file.")
    #
    # output_path = input("Enter pathname of target AWS deployment: ")
    # if not path.exists(output_path):
    #    sys.exit ("Error: invalid pathname for target credentials file.")
    #
    # print("Input path: " + input_path)
    # print("Output path: " + output_path)
