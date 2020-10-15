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

def scans_delete():

    endpoint_url = API_ROOT % "scans/delete"
    parser = argparse.ArgumentParser(description='Deletes scan data.')
    parser.add_argument('-id', '-scanid', type=str, nargs='+', help='The identifiers of scans.', required=True)
    args = parser.parse_args()

    response = requests.post(endpoint_url, json=args.id, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The scan(s) has been deleted.")

    else:
        print(response.text)

def main():

    scans_delete()

if __name__ == '__main__':
    main()