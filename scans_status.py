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

def scans_status():

    endpoint_url = API_ROOT % "scans/status/%s"
    parser = argparse.ArgumentParser(description='Gets the status of a scan.')
    parser.add_argument('-id', '-scanid', type=str, help='The identifier of scan.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        for key, value in json_response.items():
            print (key, ":", value)


        print("Response: %s - %s" % (response.status_code, response.reason))

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scans_status()

if __name__ == '__main__':
    main()