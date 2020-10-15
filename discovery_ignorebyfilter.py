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

def discovery_ignorebyfilter():

    endpoint_url = API_ROOT % "discovery/listbyfilter"
    parser = argparse.ArgumentParser(description='Ignores discovery services for selected filters.')
    parser.add_argument('-a', '-auth', type=str, help='The authority.')
    parser.add_argument('-ip', '-ipaddress', type=str, help='The ip address')
    parser.add_argument('-sd', '-sclvdm', type=str, help='The second level domain')
    parser.add_argument('-td', '-tplvdm', type=str, help='The top level domain.')
    parser.add_argument('-on', '-orgnm', type=str, help='The organization name')
    parser.add_argument('-d', '-distance', type=str, help='The distance.')
    parser.add_argument('-rd', '-regdmn', type=str, choices=['true', 'false'], default=['true'], help='The registered domain.')

    args = parser.parse_args()

    parameters = {
        'authority': args.a,
        'ipAddress': args.ip, 
        'secondLevelDomain': args.sd, 
        'topLevelDomain': args.td,
        'organizationName': args.on,
        'distance': args.d,
        'registeredDomain': args.rd,
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Discovery_IgnoreByFilter.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The services are saved into the 'Discovery_IgnoreByFilter.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    discovery_ignorebyfilter()

if __name__ == '__main__':
    main()