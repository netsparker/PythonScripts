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

def websitegroups_new():

    endpoint_url = API_ROOT % "websitegroups/new"
    parser = argparse.ArgumentParser(description='Creates a website group.')
    parser.add_argument('-gn', '-groupname', type=str, help='Gets or sets the website group name', required=True)
    args = parser.parse_args()

    agent_json = {'Name': args.gn}

    response = requests.post(endpoint_url, json=agent_json, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The website group has been created.")

    else:
        print(response.text)


def main():

    websitegroups_new()

if __name__ == '__main__':
    main()