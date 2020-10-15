import requests
import json

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def teammembers_gettimezones():
    endpoint_url = API_ROOT % "teammembers/gettimezones"
    response = requests.get(endpoint_url, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        for x in json_response:
            for x, y in x.items():
                print(x,': ', y)
        
        print("Response: %s - %s" % (response.status_code, response.reason))

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    teammembers_gettimezones()

if __name__ == '__main__':
    main()