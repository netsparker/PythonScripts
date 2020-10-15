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

def websites_sendverificationemail():

    endpoint_url = API_ROOT % "websites/sendverificationemail"
    parser = argparse.ArgumentParser(description='Sends the verification email if verification limit not exceeded yet.')
    parser.add_argument('-u', '-url', type=str, help='The website URL.', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.u, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200 and response.status_code != 201:
        print(response.text)

def main():

    websites_sendverificationemail()

if __name__ == '__main__':
    main()