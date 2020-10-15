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

def scans_incremental():

    endpoint_url = API_ROOT % "scans/incremental"
    parser = argparse.ArgumentParser(description='Launches an incremental scan based on the provided base scan identifier.')
    parser.add_argument('-id', '-scanid', type=str, help='Gets or sets the base scan identifier. Base scan should be in completed state. Currently running or cancelled scans are not valid.', required=True)
    parser.add_argument('-xe', '-imsde', type=str, choices=['true', 'false'], help='Gets or sets a value indicating whether max scan duration is enabled')
    parser.add_argument('-max', '-msd', type=int, help='Gets or sets the maximum duration of the scan in hours')
    parser.add_argument('-an', '-agent', type=str, help='Gets or sets the agent name')
    args = parser.parse_args()

    json_object = {
        'BaseScanId': args.id,
        'IsMaxScanDurationEnabled': args.xe,
        'MaxScanDuration': args.max,
        'AgentName': args.an
        }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 201):
        print("The incremental scan has been started.")

    else:
        print(response.text)

def main():

    scans_incremental()

if __name__ == '__main__':
    main()