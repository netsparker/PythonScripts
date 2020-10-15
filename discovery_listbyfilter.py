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

def discovery_listbyfilter():

    endpoint_url = API_ROOT % "discovery/listbyfilter"
    parser = argparse.ArgumentParser(description='Gets the list discovery services with filter.')
    parser.add_argument('-a', '-auth', type=str, help='The authority.')
    parser.add_argument('-ip', '-ipaddress', type=str, help='The ip address')
    parser.add_argument('-sd', '-sclvdm', type=str, help='The second level domain.')
    parser.add_argument('-td', '-tplvdm', type=str, help='The top level domain.')
    parser.add_argument('-on', '-orgnm', type=str, help='The organization name.')
    parser.add_argument('-d', '-distance', type=str, help='The distance.')
    parser.add_argument('-rd', '-regdmn', type=str, choices=['true', 'false'], default=['true'], help='The registered domain.')
    parser.add_argument('-s', '-status', type=str, choices = ['New', 'Ignored', 'Created'], default = ['New'], help='The status. Default value New')

    args = parser.parse_args()

    parameters = {
        'authority': args.a,
        'ipAddress': args.ip, 
        'secondLevelDomain': args.sd, 
        'topLevelDomain': args.td,
        'organizationName': args.on,
        'distance': args.d,
        'registeredDomain': args.rd,
        'status': args.s,
        'page': 1,
        'pageSize': 200
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Discovery_ListByFilter.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Discovery_ListByFilter.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The discovery list is saved into the 'Discovery_ListByFilter.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    discovery_listbyfilter()

if __name__ == '__main__':
    main()