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

def notifications_delete():

    endpoint_url = API_ROOT % "notifications/delete"
    parser = argparse.ArgumentParser(description='Deletes an existing scan notification definition.')
    parser.add_argument('-id', '-nid', type=str, help='Gets or sets the scan notification identifier', required=True)
    args = parser.parse_args()

    json_object = {'Id': args.id}

    response = requests.post(endpoint_url, json=json_object, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The notification has been deleted.")

    else:
        print(response.text)

def main():

    notifications_delete()

if __name__ == '__main__':
    main()