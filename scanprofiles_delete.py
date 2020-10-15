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

def scanprofiles_delete():

    endpoint_url = API_ROOT % "scanprofiles/delete"
    parser = argparse.ArgumentParser(description='Deletes a scan profiles.')
    parser.add_argument('-id', '-pid', type=str, help='The scan profiles ID.', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.n, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200 and response.status_code != 201:
        print(response.text)

def main():

    scanprofiles_delete()

if __name__ == '__main__':
    main()