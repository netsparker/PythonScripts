import requests
import argparse
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scans_schedule():

    endpoint_url = API_ROOT % "scans/schedule"
    parser = argparse.ArgumentParser(description='Schedules a scan to be launched in the future.')
    parser.add_argument('-s', '-scan', type=str, choices=["Form", "Basic", "Header", "OAuth2"], help='Scan Content', required=True)
    args = parser.parse_args()

    if args.s == "Form":
        scan = "Scans_ScheduleFormAuth.json"

    elif args.s == "Basic":
        scan = "Scans_ScheduleBasicAuth.json"
    
    elif args.s == "Header":
        scan = "Scans_ScheduleHeaderAuth.json"
    
    elif args.s == "OAuth2":
        scan = "Scans_ScheduleOAuth2.json"
    
    file = open(scan, "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Scan has been scheduled.")

def main():

    scans_schedule()

if __name__ == '__main__':
    main()