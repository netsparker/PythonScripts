import requests
import json
import argparse
import csv

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def issues_report():

    endpoint_url = API_ROOT % "issues/report"
    parser = argparse.ArgumentParser(description='Returns the report of issues in the csv format.')
    parser.add_argument('-se', '-csvSeparator', type=str, choices=['Comma', 'Semicolon', 'Pipe', 'Tab'], help='Gets or sets the csv separator.')
    parser.add_argument('-s', '-severity', type=str, choices=['BestPractice', 'Information', 'Low', 'Medium', 'High', 'Critical'], help='Gets or sets the vulnerabilitys severity.')
    parser.add_argument('-w', '-webSiteName', type=str, help='Gets or sets the websites name.')
    parser.add_argument('-wg', '-webSiteGroupName', type=str, help='Gets or sets the website groups name.')
    
    args = parser.parse_args()

    parameters = {
        'csvSeparator': args.se,
        'severity': args.s, 
        'webSiteName': args.w, 
        'webSiteGroupName': args.wg
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        with open('Issues_Report.csv', 'w', encoding='utf8') as wf:
            wf.write(response.text)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The issues report has been saved into the 'Issues_Report.csv' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    issues_report()

if __name__ == '__main__':
    main()