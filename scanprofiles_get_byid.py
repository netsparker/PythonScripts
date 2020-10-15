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

def scanprofiles_get_byid():

    endpoint_url = API_ROOT % "scanprofiles/get/%s"
    parser = argparse.ArgumentParser(description='Gets the scan profiles by the specified id.')
    parser.add_argument('-id', '-pid', type=str, help='The identifier of scan profiles.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        print("Response: %s - %s" % (response.status_code, response.reason))

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scanprofiles_get_byid()

if __name__ == '__main__':
    main()