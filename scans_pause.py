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

def scans_pause():

    endpoint_url = API_ROOT % "scans/pause"
    parser = argparse.ArgumentParser(description='Pauses a scan in progress.')
    parser.add_argument('-id', '-scanid', type=str, help='The identifier of scan.', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.id, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 201):
        print("The scan has been paused.")

    else:
        print(response.text)

def main():

    scans_pause()

if __name__ == '__main__':
    main()