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

def websites_delete():

    endpoint_url = API_ROOT % "websites/delete"
    parser = argparse.ArgumentParser(description='Deletes a website.')
    parser.add_argument('-ru', '-rooturl', type=str, help='Gets or sets the root URL', required=True)
    args = parser.parse_args()

    agent_json = {'RootUrl': args.ru}

    response = requests.post(endpoint_url, json=agent_json, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The website has been deleted.")

    else:
        print(response.text)


def main():

    websites_delete()

if __name__ == '__main__':
    main()