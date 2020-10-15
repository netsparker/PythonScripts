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

def teammembers_getbyemail():

    endpoint_url = API_ROOT % "teammembers/getbyemail"
    parser = argparse.ArgumentParser(description='Gets user by email.')
    parser.add_argument('-e', '-email', type=str, help='The email address of the user.', required=True)
    args = parser.parse_args()

    parameters = {'email': args.e}

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)   

    if (response.status_code == 200):
        
        print("Response: %s - %s" % (response.status_code, response.reason))

        json_response = response.json()
        
        for x, y in json_response.items():
            print (x ,y)

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    teammembers_getbyemail()

if __name__ == '__main__':
    main()