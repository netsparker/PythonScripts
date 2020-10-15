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

def scanpolicies_delete():

    endpoint_url = API_ROOT % "scanpolicies/delete"
    parser = argparse.ArgumentParser(description='Deletes a scan policy.')
    parser.add_argument('-n', '-pname', type=str, help='The scan policy name.', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.n, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The scan policy has been deleted.")

    else:
        print(response.text)

def main():

    scanpolicies_delete()

if __name__ == '__main__':
    main()