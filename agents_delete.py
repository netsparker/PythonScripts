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

def agents_delete():

    endpoint_url = API_ROOT % "agents/delete"
    parser = argparse.ArgumentParser(description='Sets agent status as terminated. Before deleting an agent, please make sure that youve stopped the related service from the Windows Services Manager screen. If it is running, the agent will reappear on the page despite removal.')
    parser.add_argument('-id', '-agentid', type=str, help='Gets or sets the unique identifier of agent', required=True)
    args = parser.parse_args()

    agent_json = {'AgentId': args.id}

    response = requests.post(endpoint_url, json=agent_json, auth=AUTH)

    print("Response: %s - %s" % (response.status_code, response.reason))
    print(response.text)

def main():

    agents_delete()

if __name__ == '__main__':
    main()