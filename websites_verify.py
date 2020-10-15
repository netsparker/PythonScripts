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

def websites_verify():

    endpoint_url = API_ROOT % "websites/verify"
    parser = argparse.ArgumentParser(description='Executes verification process.')

    parser.add_argument('-vm', '-method', type=str, choices = ['File', 'Tag', 'Dns', 'Email'], help='Gets or sets the verification method')
    parser.add_argument('-vs', '-secret', type=str, help='Gets or sets the verification secret')
    parser.add_argument('-u', '-url', type=str, help='Gets or sets the website URL', required=True)

    args = parser.parse_args()

    json_object = {
        'VerificationMethod': args.vm,
        'VerificationSecret': args.vs,
        'WebsiteUrl': args.u
        }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The website has been verified.")

    else:
        print(response.text)


def main():

    websites_verify()

if __name__ == '__main__':
    main()