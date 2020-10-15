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

def scans_listbystate():

    endpoint_url = API_ROOT % "scans/listbystate"
    parser = argparse.ArgumentParser(description='Gets the list of scans by state.')
    parser.add_argument('-s', '-state', type=str, choices=['Queued', 'Scanning', 'Archiving', 'Complete', 'Failed', 'Cancelled', 'Delayed', 'Pausing', 'Paused', 'Resuming'], help='The state of ScanTask.', required=True)
    parser.add_argument('-uc', '-urlcrit', type=str, help='Enter the search criteria that contains the Target URL of scan')
    parser.add_argument('-sd', '-startd', type=str, help='The start date is used for scan StateChanged field and it is less than or equal to StateChanged field. If scanTask field set as Queued, the start date is used for scan Initiated field.Format: MM/dd/yyyy 00:00:00')
    parser.add_argument('-ed', '-endd', type=str, help='The end date is used for scan StateChanged field and it is greater than or equal to StateChanged field. If scanTask field set as Queued, the end date is used for scan Initiated field.Format: MM/dd/yyyy 23:59:59')

    args = parser.parse_args()

    parameters = {
        'scanTaskState': args.s,
        'targetUrlCriteria': args.uc,
        'page': 1, 
        'pageSize': 200,
        'startDate': args.sd,
        'endDate': args.ed
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Scans_ListByState.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Scans_ListByState.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan list is saved into the 'Scans_ListByState.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    scans_listbystate()

if __name__ == '__main__':
    main()