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

def websitegroups_get():

    endpoint_url = API_ROOT % "websitegroups/get"
    parser = argparse.ArgumentParser(description='Gets website group by name.')
    parser.add_argument('-gn', '-groupname', type=str, help='Gets or sets the website group name', required=True)
    args = parser.parse_args()

    parameters = {
        'query': args.gn
    }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('WebsiteGroups_Get.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The website group info is saved into the 'WebsiteGroups_Get.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    websitegroups_get()

if __name__ == '__main__':
    main()