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

def scans_downloadscanfile():

    endpoint_url = API_ROOT % "scans/downloadscanfile"
    parser = argparse.ArgumentParser(description='Downloads the scan file as zip.')
    parser.add_argument('-id', '-scanid', type=str, help='The scan id', required=True)
    
    args = parser.parse_args()

    parameters = {
        'scanId': args.id
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if (response.status_code != 200):
        print(response.text)

    else:
        with open('scandata.zip', 'wb') as f:
            f.write(response.content)
        
        print("Scan file has been downloaded. It is saved to scandata.zip")

def main():

    scans_downloadscanfile()

if __name__ == '__main__':
    main()