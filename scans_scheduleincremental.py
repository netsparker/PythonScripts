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

def scans_scheduleincremental():

    endpoint_url = API_ROOT % "scans/schedule-incremental"
    parser = argparse.ArgumentParser(description='Schedules an incremental scan to be launched in the future.')
    parser.add_argument('-me', '-maxsde', type=str, choices=['true', 'false'], help='Gets or sets a value indicating whether max scan duration is enabled')
    parser.add_argument('-max', '-maxscand', type=int, help='Gets or sets the maximum duration of the scan in hours')
    parser.add_argument('-n', '-name', type=str, help='Gets or sets the name', required=True)
    parser.add_argument('-nt', '-nextet', type=str, help='Gets or sets the next execution time. Date string must be in the same format as in the account settings', required=True)
    parser.add_argument('-st', '-srunt', type=str, choices=['Once', 'Daily', 'Weekly', 'Monthly', 'Quarterly', 'Biannually', 'Yearly', 'Custom'], help='Gets or sets the run interval of scheduled scan', required=True)
    parser.add_argument('-an', '-agentn', type=str, help='Gets or sets the agent name')
    parser.add_argument('-id', '-scanid', type=str, help='Gets or sets the base scan identifier', required=True)

    args = parser.parse_args()

    json_object = {
        'IsMaxScanDurationEnabled': args.me,
        'MaxScanDuration': args.max,
        'Name': args.n,
        'NextExecutionTime': args.nt,
        'ScheduleRunType': args.st,
        'AgentName': args.an,
        'BaseScanId': args.id
    }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 201):
        print("The scan has been scheduled.")

    else:
        print(response.text)

def main():

    scans_scheduleincremental()

if __name__ == '__main__':
    main()