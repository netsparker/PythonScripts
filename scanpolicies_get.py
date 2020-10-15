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

def scanpolicies_get():

    endpoint_url = API_ROOT % "scanpolicies/get"
    parser = argparse.ArgumentParser(description='Gets the scan policy by the specified name.')
    parser.add_argument('-n', '-pname', type=str, help='The scan policy name.', required=True)

    args = parser.parse_args()

    parameters = {'name': args.n}

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        with open('ScanPolicies_Get.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan policy info has been saved into the 'ScanPolicies_Get.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scanpolicies_get()

if __name__ == '__main__':
    main()