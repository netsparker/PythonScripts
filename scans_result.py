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

def scans_result():

    endpoint_url = API_ROOT % "scans/result/%s"
    parser = argparse.ArgumentParser(description='Gets the result of a scan.')
    parser.add_argument('-id', '-scanid', type=str, help='The identifier of scan.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.get(endpoint_url, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Scans_Result.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The issues are saved into the 'Scans_Result.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scans_result()

if __name__ == '__main__':
    main()