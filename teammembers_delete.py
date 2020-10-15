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

def teammembers_delete():

    endpoint_url = API_ROOT % "teammembers/delete/%s"
    parser = argparse.ArgumentParser(description='Deletes a user.')
    parser.add_argument('-id', '-uid', type=str, help='The identifier of the user.', required=True)
    args = parser.parse_args()

    endpoint_url = endpoint_url % args.id

    response = requests.post(endpoint_url, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))

    if (response.status_code == 200):
        print("The team member has been deleted.")

    else:
        print(response.text)

def main():

    teammembers_delete()

if __name__ == '__main__':
    main()