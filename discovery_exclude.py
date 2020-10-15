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


def discovery_exclude():

    endpoint_url = API_ROOT % "discovery/exclude"
    parser = argparse.ArgumentParser(description='Returns exclude operation result. This operation note override existing data, append to existing data. If you want to override please use update-settings endpoint.')
    parser.add_argument('-s', '-slds', type=str, help='Gets or sets the excluded SLDS')
    parser.add_argument('-t', '-tlds', type=str, help='Gets or sets the excluded TLDS')
    parser.add_argument('-ip', '-ipaddress', type=str, help='Gets or sets the excluded ip addresses')
    parser.add_argument('-d', '-domains', type=str, help='Gets or sets the excluded domains')
    parser.add_argument('-o', '-orgs', nargs='+', help='Gets or sets the excluded organizations')
    args = parser.parse_args()

    json_object = {
        "ExcludedSlds": args.s,
        "ExcludedTlds": args.t,
        "ExcludedIpAddresses": args.ip,
        "ExcludedDomains": args.d,
        "ExcludedOrganizations": args.o
        }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    print(response.text)


def main():

    discovery_exclude()

if __name__ == '__main__':
    main()