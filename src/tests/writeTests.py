import boto3
import sys
import pprint
from boto3 import Session
from write_infra import scriptTemplates
from write_infra import createScripts


from utils import credential

if __name__ == "__main__":
    creds = credential.Credential ("output", "us-west-1")
    try:
        session = Session(profile_name="input")
        session_creds = session.get_credentials()
        # Credentials are refreshable, so accessing your access key / secret key
        # separately can lead to a race condition. Use this to get an actual matched
        # set.
        frozen_creds = session_creds.get_frozen_credentials()
        creds.set_access_key(frozen_creds.access_key)
        creds.set_secret_key(frozen_creds.secret_key)

    except:
        sys.exit("Error: invalid profile.")

    if not creds.region:
        sys.exit("Error: invalid region.")

    profile = creds.profile
    region = creds.region

    for key in scriptTemplates.scripts.keys():
        scriptTemplates.scripts[key] = createScripts.replace_profile_and_region(scriptTemplates.scripts[key], profile, region)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(scriptTemplates.scripts)
