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

def scanprofiles_new():

    endpoint_url = API_ROOT % "scanprofiles/new"

    parser = argparse.ArgumentParser(description='Select a sample profile')
    parser.add_argument('-p', '-profile', type=str, choices=["Form", "Basic", "Header", "OAuth2"], help='Profile Content', required=True)
    args = parser.parse_args()

    if args.p == "Form":
        profile = "ScanProfiles_NewSampleForm.json"

    elif args.p == "Basic":
        profile = "ScanProfiles_NewSampleBasic.json"
    
    elif args.p == "Header":
        profile = "ScanProfiles_NewSampleHeader.json"
    
    elif args.p == "OAuth2":
        profile = "ScanProfiles_NewSampleOAuth2.json"
    
    file = open(profile, "r")
    json_object = json.load(file)
    file.close()

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Scan profile has been created.")

def main():

    scanprofiles_new()

if __name__ == '__main__':
    main()