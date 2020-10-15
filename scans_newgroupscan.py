import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scans_newgroupscan():

    endpoint_url = API_ROOT % "scans/newgroupscan"

    jsonf = "Scans_NewGroupScanSample.json"
    
    file = open(jsonf, "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Group Scan has been launched.")

def main():

    scans_newgroupscan()

if __name__ == '__main__':
    main()