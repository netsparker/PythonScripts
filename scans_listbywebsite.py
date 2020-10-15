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

def scans_listbywebsite():

    endpoint_url = API_ROOT % "scans/listbywebsite"
    parser = argparse.ArgumentParser(description='Gets the list of scans and their details.')

    parser.add_argument('-w', '-wurl', type=str, help='The website URL.')
    parser.add_argument('-t', '-turl', type=str, help='The target URL of the scan.')
    parser.add_argument('-ds', '-sort', type=str, choices=['Ascending', 'Descending'], help='The initiated date sort type.')

    args = parser.parse_args()

    parameters = {
        'websiteUrl': args.w,
        'targetUrl': args.t,
        'page': 1, 
        'pageSize': 200,
        'initiatedDateSortType': args.ds
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Scans_ListByWebsite.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Scans_ListByWebsite.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan list is saved into the 'Scans_ListByWebsite.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    scans_listbywebsite()

if __name__ == '__main__':
    main()