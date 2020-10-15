import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scanprofiles_update():

    endpoint_url = API_ROOT % "scanprofiles/update"

    # Change the profile name accordingly;
    
    profile = "ScanProfiles_UpdateSample.json"

    file = open(profile, "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200:
        print(response.text)

    else:
        print("Scan profile has been updated.")

def main():

    scanprofiles_update()

if __name__ == '__main__':
    main()