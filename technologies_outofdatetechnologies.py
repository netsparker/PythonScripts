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

def technologies_outofdatetechnologies():

    endpoint_url = API_ROOT % "technologies/outofdatetechnologies"
    parser = argparse.ArgumentParser(description='Gets the list of out-of-date technologies that currently in use.')
    parser.add_argument('-w', '-website', type=str, help='The websites name.')
    parser.add_argument('-t', '-techn', type=str, help='The technologys display name.')

    args = parser.parse_args()

    parameters = {
        'webSiteName': args.w,
        'technologyName': args.t,
        'page': 1, 
        'pageSize': 200
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        json_list = json_response['List']
            
        with open('Technologies_OutOfDateTechnologies.json', 'w') as outfile:
            json.dump(json_list, outfile, indent=4)

        while json_response['HasNextPage'] is True:

            parameters['page'] += 1
            response = requests.get(endpoint_url, params=parameters, auth=AUTH)
            json_response = response.json()

            json_list += json_response['List']

            with open('Technologies_OutOfDateTechnologies.json', 'w') as outfile:
                json.dump(json_list, outfile, indent=4)


        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The Out-of-Date Technologies list is saved into the 'Technologies_OutOfDateTechnologies.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)
        
def main():

    technologies_outofdatetechnologies()

if __name__ == '__main__':
    main()