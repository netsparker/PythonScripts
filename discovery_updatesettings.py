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

def discovery_updatesettings():

    endpoint_url = API_ROOT % "discovery/update-settings"
    parser = argparse.ArgumentParser(description='Updates discovery settings.')
    parser.add_argument('-isl', '-islds', type=str, help='Gets or sets the included SLDS')
    parser.add_argument('-ii', '-iiprng', type=str, help='Gets or sets the included ip ranges')
    parser.add_argument('-io', '-iorgs', type=str, help='Gets or sets the included organizations')
    parser.add_argument('-es', '-eslds', type=str, help='Gets or sets the excluded SLDS')
    parser.add_argument('-et', '-etlds', type=str, help='Gets or sets the excluded TLDS')
    parser.add_argument('-ei', '-eipadr', type=str, help='Gets or sets the excluded ip addresses')
    parser.add_argument('-eo', '-eorgs', type=str, help='Gets or sets the excluded organizations')
    parser.add_argument('-ord', '-onredo', type=str, choices=['true', 'false'], default = 'false', help='Gets or sets a value indicating whether [only registered domains]')
    parser.add_argument('-sh', '-shhoma', type=str, choices=['true', 'false'], default = 'false', help='Gets or sets a value indicating whether [shared host matching]')
    parser.add_argument('-on', '-ornmmt', type=str, choices=['true', 'false'], default = 'false', help='Gets or sets a value indicating whether [organization name matching]')
    parser.add_argument('-em', '-emamt', type=str, choices=['true', 'false'], default = 'false', help='Gets or sets a value indicating whether [email matching]')
    parser.add_argument('-wm', '-webmt', type=str, choices=['true', 'false'], default = 'false', help='Gets or sets a value indicating whether [websites matching]')

    args = parser.parse_args()

    json_object = {
        "IncludedSlds": args.isl,
        "IncludedIpRanges": args.ii,
        "IncludedOrganizations": args.io,
        "ExcludedSlds": args.es,
        "ExcludedTlds": args.et,
        "ExcludedIpAddresses": args.ei,
        "ExcludedOrganizations": args.eo,
        "OnlyRegisteredDomains": args.ord,
        "SharedHostMatching": args.sh,
        "OrganizationNameMatching": args.on,
        "EmailMatching": args.em,
        "WebsitesMatching": args.wm
        }

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The settings have been updated.")

    else:
        print(response.text)

def main():

    discovery_updatesettings()

if __name__ == '__main__':
    main()