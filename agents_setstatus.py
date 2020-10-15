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

def agents_setstatus():

    endpoint_url = API_ROOT % "agents/setstatus"
    parser = argparse.ArgumentParser(description='Sets agent status enable or disable.')
    parser.add_argument('-id', '-agentid', type=str, help='Gets or sets the unique identifier of agent', required=True)
    parser.add_argument('-s', '-status', type=str, help='Gets or sets a value that represents the status of this agent instance', required=True)
    args = parser.parse_args()

    agent_json = {'AgentId': args.id, 'Status': args.s} 
    
    response = requests.post(endpoint_url, json=agent_json, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    print(response.text)

def main():

    agents_setstatus()

if __name__ == '__main__':
    main()