import os
import sys
from boto3 import Session

class Credential:
    def __init__(self, profile, region):
        self.profile = profile
        self.region = region
        os.environ['AWS_DEFAULT_REGION'] = self.region

    def set_access_key (self, access_key):
        self.access_key = access_key

    def set_secret_key (self, secret_key):
        self.secret_key = secret_key


def get_credentials():
    profile = input("Enter profile name of AWS deployment: ")
    region = input("Enter region of AWS deployment: ")
    os.environ['AWS_DEFAULT_REGION'] = region

    creds = Credential(profile, region)
    try:
        session = Session(profile_name=profile)
        session_creds = session.get_credentials()
        # Credentials are refreshable, so accessing your access key / secret key
        # separately can lead to a race condition. Use this to get an actual matched
        # set.
        frozen_creds = session_creds.get_frozen_credentials()
        creds.set_access_key(frozen_creds.access_key)
        creds.set_secret_key(frozen_creds.secret_key)

    except:
        sys.exit("Error: invalid profile: " + profile)

    if not region:
        sys.exit("Error: invalid region: " + region)

    return creds
