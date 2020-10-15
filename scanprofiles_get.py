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

def scanprofiles_get():

    endpoint_url = API_ROOT % "scanprofiles/get"
    parser = argparse.ArgumentParser(description='Gets the scan profiles by the specified name.')
    parser.add_argument('-n', '-pname', type=str, help='The scan profiles name.', required=True)

    args = parser.parse_args()

    parameters = {'name': args.n}

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        print("Response: %s - %s" % (response.status_code, response.reason))

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scanprofiles_get()

if __name__ == '__main__':
    main()