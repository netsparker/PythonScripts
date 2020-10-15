import requests
import json
import argparse

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scans_newwithprofile():

    endpoint_url = API_ROOT % "scans/newwithprofile"
    parser = argparse.ArgumentParser(description='Launches a new scan with profile id.')
    parser.add_argument('-p', '-pname', type=str, help='Gets or sets the profile id', required=True)
    parser.add_argument('-u', '-target', type=str, help='Gets or sets the target URI', required=True)
    args = parser.parse_args()

    agent_json = {
        'ProfileName': args.p,
        'TargetUri': args.u
        }

    response = requests.post(endpoint_url, json=agent_json, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 201):

        print("The scan has been started.")

    else:
        print(response.text)

def main():

    scans_newwithprofile()

if __name__ == '__main__':
    main()