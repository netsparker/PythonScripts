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

def issues_waitingforretest():

    endpoint_url = API_ROOT % "issues/waitingforretest"
    parser = argparse.ArgumentParser(description='Gets the list of retest issues.')
    parser.add_argument('-s', '-severity', type=str, choices=['BestPractice', 'Information', 'Low', 'Medium', 'High', 'Critical'], help='The vulnerability severity')
    parser.add_argument('-w', '-webSiteName', type=str, help='The websites name.')
    parser.add_argument('-wg', '-webSiteGroupName', type=str, help='The website groups name.')
    args = parser.parse_args()

    parameters = {
        'severity': args.s, 
        'webSiteName': args.w, 
        'webSiteGroupName': args.wg, 
        'page': 1, 
        'pageSize': 200
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Issues_WaitingForRetest.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Issues_WaitingForRetest.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The issues list is saved into the 'Issues_WaitingForRetest.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    issues_waitingforretest()

if __name__ == '__main__':
    main()