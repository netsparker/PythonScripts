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

def websites_update():

    endpoint_url = API_ROOT % "websites/update"
    parser = argparse.ArgumentParser(description='Updates a website.')
    parser.add_argument('-p', '-protocol', type=str, choices = ['Http', 'Https'], help='Gets or sets the default protocol')
    parser.add_argument('-am', '-agentmode', type=str, choices=['Cloud', 'Internal'], default="Cloud", help='Gets or sets the agent mode for the website')
    parser.add_argument('-ru', '-rooturl', type=str, help='Gets or sets the root URL', required=True)
    parser.add_argument('-wg', '-groups', type=str, nargs='*', help='Gets or sets the name of groups this website will belong to')
    parser.add_argument('-lt', '-license', type=str, choices=['Subscription', 'Credit'], help='Gets or sets the type of the subscription', required=True)
    parser.add_argument('-n', '-name', type=str, help='Gets or sets the website name', required=True)
    parser.add_argument('-ce', '-techmail', type=str, help='Gets or sets the technical contact email')

    args = parser.parse_args()

    json_object = {
        'DefaultProtocol': args.p,
        'AgentMode': args.am,
        'RootUrl': args.ru,
        'Groups': args.wg,
        'LicenseType': args.lt,
        'Name': args.n,
        'TechnicalContactEmail': args.ce
        }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The website has been updated.")

    else:
        print(response.text)


def main():

    websites_update()

if __name__ == '__main__':
    main()