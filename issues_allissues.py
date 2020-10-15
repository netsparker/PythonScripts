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

def issues_allissues():

    endpoint_url = API_ROOT % "issues/allissues"
    parser = argparse.ArgumentParser(description='Gets the list of all issues.')
    parser.add_argument('-s', '-severity', type=str, choices=['BestPractice', 'Information', 'Low', 'Medium', 'High', 'Critical'], help='The vulnerability severity')
    parser.add_argument('-w', '-webSiteName', type=str, help='The websites name')
    parser.add_argument('-wg', '-webSiteGroupName', type=str, help='The website groups name')
    parser.add_argument('-st', '-sortType', type=str, choices=['Ascending', 'Descending'], default="Ascending", help='Sort by ascending and descending according to LastSeenDate. Default parameter ascending.')
    parser.add_argument('-l', '-lastSeenDate', type=str, help='You can use the date format defined in your account. You can visit /account/changesettings to view the current format.')
    parser.add_argument('-r', '-rawDetails', type=str, choices=['true', 'false'], default='true', help='If you want the vulnerability data response(Remedy, Description etc.) to return without raw html, this field must be set false.')

    args = parser.parse_args()

    parameters = {
        'severity': args.s, 
        'webSiteName': args.w, 
        'webSiteGroupName': args.wg, 
        'page': 1, 
        'pageSize': 200,
        'sortType:': args.st,
        'lastSeenDate': args.l,
        'rawDetails': args.r
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Issues_AllIssues.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Issues_AllIssues.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The issues list is saved into the 'Issues_AllIssues.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    issues_allissues()

if __name__ == '__main__':
    main()