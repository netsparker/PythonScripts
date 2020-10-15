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

def websites_getwebsitesbygroup():

    endpoint_url = API_ROOT % "websites/getwebsitesbygroup"
    parser = argparse.ArgumentParser(description='Gets the list of websites by group name or id.')
    parser.add_argument('-gi', '-groupinfo', type=str, help='The website group name or URL.', required=True)

    args = parser.parse_args()

    parameters = {
        'query': args.gi,
        'page': 1, 
        'pageSize': 200
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Websites_GetWebsitesByGroup.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Websites_GetWebsitesByGroup.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The websites are saved into the 'Websites_GetWebsitesByGroup.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    websites_getwebsitesbygroup()

if __name__ == '__main__':
    main()