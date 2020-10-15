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

def notifications_setpriorities():

    endpoint_url = API_ROOT % "notifications/setpriorities"
    parser = argparse.ArgumentParser(description='Sets the priorities of notifications.')
    parser.add_argument('-id', '-nid', type=str, help='Gets or sets the identifier', required=True)
    parser.add_argument('-p', '-priority', type=int, help='Gets or sets the priority', required=True)

    args = parser.parse_args()

    json_object = {"Id": args.id, "Priority": args.p}

    request_body = [json_object]
    
    response = requests.post(endpoint_url, request_body, auth=AUTH)

    response_info(response)

def response_info(response):

    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200 and response.status_code != 201:
        print(response.text)

def main():

    notifications_setpriorities()

if __name__ == '__main__':
    main()