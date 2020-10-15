import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def account_license():
    
    endpoint_url = API_ROOT % "account/license"
    response = requests.get(endpoint_url, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()
        print("\nLicenses:")
        for x in json_response["Licenses"]:
        
            print("License ID: %s" % (x["Id"]))
            print("Is Active?: %s" % (x["IsActive"]))
            print("Valid For Days: %s" % (x["ValidForDays"]))
            print("Response: %s - %s" % (response.status_code, response.reason))

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    account_license()

if __name__ == '__main__':
    main()