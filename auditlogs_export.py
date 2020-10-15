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

def auditlogs_export():

    endpoint_url = API_ROOT % "auditlogs/export"
    parser = argparse.ArgumentParser(description='Returns the selected log type in the csv format as a downloadable file.')
    parser.add_argument('-s', '-csvSeperator', type=str, choices=['Comma', 'Semicolon', 'Pipe', 'Tab'], help='The csv separator. Default comma (,)')
    parser.add_argument('-sd', '-startDate', type=str, help='The start date is used for logs and it is less than or equal to Date field.Format: MM/dd/yyyy 00:00:00 . Default: Account creation date', default="01/01/2015 00:00:01")
    parser.add_argument('-ed', '-endDate', type=str, help='The end date is used for logs and it is greather than or equal to Date field.Format: MM/dd/yyyy 23:59:59 . Default: Current time')

    args = parser.parse_args()

    parameters = {
        'csvSeparator': args.s,
        'startDate': args.sd,
        'endDate': args.ed
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        with open('AuditLogs.csv', 'w', encoding='utf8') as wf:
            wf.write(response.text)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The logs are saved into the 'AuditLogs.csv' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    auditlogs_export()

if __name__ == '__main__':
    main()