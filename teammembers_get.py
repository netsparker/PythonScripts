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

def teammembers_get():

    endpoint_url = API_ROOT % "teammembers/get/%s"
    parser = argparse.ArgumentParser(description='Gets user by id.')
    parser.add_argument('-id', '-uid', type=str, help='The id of the user.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()
        
        print("Response: %s - %s" % (response.status_code, response.reason))
        
        for x, y in json_response.items():
            print (x ,y)

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    teammembers_get()

if __name__ == '__main__':
    main()