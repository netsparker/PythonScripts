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

def discovery_export():

    endpoint_url = API_ROOT % "discovery/export"
    parser = argparse.ArgumentParser(description='Returns the all discovery services in the csv format as a downloadable file.')
    parser.add_argument('-s', '-csvSeperator', type=str, choices=['Comma', 'Semicolon', 'Pipe', 'Tab'], default=['Comma'], help='The csv separator. Default comma (,)')

    args = parser.parse_args()

    parameters = {
        'csvSeparator': args.s
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        with open('Discovery_Export.csv', 'w', encoding='utf8') as wf:
            wf.write(response.text)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The services have been saved into the 'Discovery_Export.csv' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    discovery_export()

if __name__ == '__main__':
    main()