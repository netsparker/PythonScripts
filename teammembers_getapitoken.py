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

def teammembers_getapitoken():

    endpoint_url = API_ROOT % "teammembers/getapitoken"
    parser = argparse.ArgumentParser(description='Gets user api token.')
    parser.add_argument('-e', '-email', type=str, help='User email address.', required=True)
    args = parser.parse_args()

    parameters = {'email': args.e}

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)   

    if (response.status_code == 200):
        
        print("Response: %s - %s" % (response.status_code, response.reason))

        json_response = response.json()
        
        for x, y in json_response.items():
            print (x, ":", y)

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    teammembers_getapitoken()

if __name__ == '__main__':
    main()