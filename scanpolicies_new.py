import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scanpolicies_new():

    endpoint_url = API_ROOT % "scanpolicies/new"

    file = open("ScanPoliciesNewSample.json", "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Scan policy has been created.")

def main():

    scanpolicies_new()

if __name__ == '__main__':
    main()