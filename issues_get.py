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

def issues_get():

    endpoint_url = API_ROOT % "issues/get/%s"
    parser = argparse.ArgumentParser(description='Gets issues by id. Returns with encoded(raw html) vulnerability template data by default.')
    parser.add_argument('-id', '-issueid', type=str, help='Issue ID', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Issues_Get.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The issues are saved into the 'Issues_Get.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    issues_get()

if __name__ == '__main__':
    main()