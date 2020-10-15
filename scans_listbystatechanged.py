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

def scans_listbystatechanged():

    endpoint_url = API_ROOT % "scans/listbystatechanged"
    parser = argparse.ArgumentParser(description='Gets the list of scans by stateChanged')

    parser.add_argument('-sd', '-startd', type=str, help='The start date is used for scan StateChanged field and it is less than or equal to StateChanged field. Format: MM/dd/yyyy 00:00:00', required=True)
    parser.add_argument('-ed', '-endd', type=str, help='The end date is used for scan StateChanged field and it is greater than or equal to StateChanged field. Format : MM/dd/yyyy 23:59:59', required=True)

    args = parser.parse_args()

    parameters = {
        'page': 1, 
        'pageSize': 200,
        'startDate': args.sd,
        'endDate': args.ed
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)

    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Scans_ListByStateChanged.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Scans_ListByStateChanged.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan list is saved into the 'Scans_ListByStateChanged.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    scans_listbystatechanged()

if __name__ == '__main__':
    main()