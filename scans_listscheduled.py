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

def scans_listscheduled():

    endpoint_url = API_ROOT % "scans/list-scheduled"
    parser = argparse.ArgumentParser(description='Gets the list of scheduled scans which are scheduled to be launched in the future.')

    args = parser.parse_args()

    parameters = {
        'page': 1, 
        'pageSize': 200,
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Scans_ListScheduled.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Scans_ListScheduled.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan list is saved into the 'Scans_ListScheduled.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    scans_listscheduled()

if __name__ == '__main__':
    main()