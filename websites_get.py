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

def websites_get():

    endpoint_url = API_ROOT % "websites/get"
    parser = argparse.ArgumentParser(description='Gets website by name or URL.')
    parser.add_argument('-wi', '-webinfo', type=str, help='The website name or URL.', required=True)
    args = parser.parse_args()

    parameters = {
        'query': args.wi
    }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Websites_Get.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The website info has been saved into the 'Websites_Get.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    websites_get()

if __name__ == '__main__':
    main()