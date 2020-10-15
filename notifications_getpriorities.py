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

def notifications_getpriorities():

    endpoint_url = API_ROOT % "notifications/getpriorities"
    parser = argparse.ArgumentParser(description='Gets the list of notifications grouped by their Scopes and ordered by priorities for the given event.')
    parser.add_argument('-e', '-event', type=str, choices=[
        'ExceptionOccurred', 
        'AgentInstanceLaunchFailed', 
        'AccessGranted', 
        'NonrespondingAgents', 
        'LongRunningScans', 
        'UserConfirmEmail',
        'UserPasswordReset',
        'UserPasswordChanged',
        'UserScanLaunched',
        'UserScanCompleted',
        'UserScanFaulted',
        'UserScanCancelled',
        'UserScheduledScanCouldntLaunched',
        'UserWebsiteVerify',
        'UserTwoFactorAuthenticationEnabled',
        'UserAccountInvitation',
        'IssueUpdated',
        'NewFormAuthenticationLogin',
        'NewGuidedUserWebsiteAdded',
        'MaxScanTimeExceeded',
        'UserGroupScanLaunched',
        'UserPhoneNumberConfirmation',
        'UserUnconfirmedPhoneNumber',
        'SupportAccessConfirmation',
        'AccountExpire',
        'AccountDelete',
        'LateConfirmationCompleted',
        'OutDatedAgent',
        'HungScans',
        'UserScansLaunched',
        'UserScansCompleted',
        'UserScansFailed',
        'UserScansCanceled',
        'UserScheduledScansFailed',
        'UserAccessTokenReset',
        'OutofDateTechnology',
        'UserCreated',
        'UserU2FSecurityKeyEnabled',
        'UserU2FSecurityKeyReConfigured'
        ], help='The notification event.', required=True)

    args = parser.parse_args()

    parameters = {'event': args.e}

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        json_response = response.json()

        with open('Notifications_GetPriorities.json', 'w') as outfile:
            json.dump(json_response, outfile, indent=4)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The notification priorities are saved into the 'Notifications_GetPriorities.json' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    notifications_getpriorities()

if __name__ == '__main__':
    main()