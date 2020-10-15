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

def websites_get_byId():

    endpoint_url = API_ROOT % "websites/get/%s"
    parser = argparse.ArgumentParser(description='Gets websites by id.')
    parser.add_argument('-id', '-webid', type=str, help='The website id.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Websites_Get_ById.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The website info has been saved into the 'Websites_Get_ById.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    websites_get_byId()

if __name__ == '__main__':
    main()