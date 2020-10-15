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

def discovery_ignore():

    endpoint_url = API_ROOT % "discovery/ignore"
    parser = argparse.ArgumentParser(description='Ignores discovery service with given service ids.')
    parser.add_argument('-id', '-serviceids', type=str, nargs='+', help='Service IDs', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.id, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    print(response.text)

def main():

    discovery_ignore()

if __name__ == '__main__':
    main()