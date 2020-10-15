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

def scans_retest():

    endpoint_url = API_ROOT % "scans/retest"
    parser = argparse.ArgumentParser(description='Launches a retest scan based on the provided base scan identifier.')
    parser.add_argument('-an', '-agentn', type=str, help='Gets or sets the agent name')
    parser.add_argument('-id', '-scanid', type=str, help='Gets or sets the base scan identifier', required=True)

    args = parser.parse_args()

    json_object = {
        'AgentName': args.an,
        'BaseScanId': args.id
    }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 201):
        print("The scan has been launched.")

    else:
        print(response.text)

def main():

    scans_retest()

if __name__ == '__main__':
    main()