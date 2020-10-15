import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scans_updatescheduled():

    endpoint_url = API_ROOT % "scans/update-scheduled"

    # Change the scan file name accordingly;

    scan = "ScansUpdateScheduledSample.json"
    
    file = open(scan, "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200:
        print(response.text)

    else:
        print("Scan has been updated.")

def main():

    scans_updatescheduled()

if __name__ == '__main__':
    main()