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

def scans_detail():

    endpoint_url = API_ROOT % "scans/detail/%s"
    parser = argparse.ArgumentParser(description='Gets the detail of a scan.')
    parser.add_argument('-id', '-scanid', type=str, help='The identifier of scan.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Scans_Detail.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan details are saved into the 'Scans_Detail.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scans_detail()

if __name__ == '__main__':
    main()