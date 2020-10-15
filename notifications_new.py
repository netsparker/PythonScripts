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

def notifications_new():

    endpoint_url = API_ROOT % "notifications/new"
    parser = argparse.ArgumentParser(description='Creates a new scan notification definition.')
    parser.add_argument('-e', '-emails', type=str, nargs='+', help='Gets or sets the emails of users who will be notified via Email')
    parser.add_argument('-eu', '-excludedUsers', type=str, nargs='+', help='Gets or sets users emails who wont be notified')
    parser.add_argument('-i', '-integrations', type=str, nargs='+', help='Gets or sets the names of integraton endpoints which will be notified')
    parser.add_argument('-pn', '-phoneNumbers', type=str, nargs='+', help='Gets or sets the phone numbers of users who will be notified via SMS')
    parser.add_argument('-se', '-semailr', type=str, nargs='+', help='Gets or sets the specific recipients who will be notified via Email')
    parser.add_argument('-ss', '-ssmsr', type=str, nargs='+', help='Gets or sets the specific recipients who will be notified via SMS')

    parser.add_argument('-wg', '-wgroupname', type=str, help='Gets or sets the website group identifier associated with this scan notification')
    parser.add_argument('-ru', '-wrooturl', type=str, help='Gets or sets the website identifier associated with this scan notification')
    parser.add_argument('-c', '-certainty', type=int, help='Gets or sets a value indicating whether this Scan Notification is certainty')
    parser.add_argument('-d', '-disabled', type=str, choices=['true', 'false'], default='true', help='Gets or sets a value indicating whether this Scan Notification is disabled', required=True)
    parser.add_argument('-ev', '-event', type=str, choices=['NewScan', 'ScanCompleted', 'ScanCancelled', 'ScanFailed', 'ScheduledScanLaunchFailed', 'OutOfDateTechnology'], help='Gets or sets the event name. This property determines when this rule will be executed', required=True)
    parser.add_argument('-ic', '-isconfirmed', type=str, choices=['true', 'false'], default='true', help='Gets or sets a value indicating whether this Scan Notification is confirmed')
    parser.add_argument('-ls', '-lowests', type=str, choices=['BestPractice', 'Information', 'Low', 'Medium', 'High', 'Critical'], help='Gets or sets the lowest severity. This property determines when this rule will be executed and is only used for Scan Completion Notification')
    parser.add_argument('-n', '-name', type=str, help='Gets or sets the name', required=True)
    parser.add_argument('-sc', '-scope', type=str, choices=['AnyWebsite', 'WebsiteGroup', 'Website'], help='Gets or sets the Website Scope. This property indicates whether this rule will be executed for a specific Website, WebsiteGroup or All Websites', required=True)

    args = parser.parse_args()

    if not (args.e or args.eu or args.i or args.pn or args.se or args.ss):
        parser.error('At least 1 recipient is required.')

    recipient_object = {
        'Emails': args.e,
        'ExcludedUsers': args.eu,
        'Integrations': args.i,
        'PhoneNumbers': args.pn,
        'SpecificEmailRecipients': args.se,
        'SpecificSmsRecipients': args.ss
        }
    
    json_object = {
        "Recipients": recipient_object,
        "WebsiteGroupName": args.wg,
        "WebsiteRootUrl": args.ru,
        "Certainty": args.c,
        "Disabled": args.d,
        "Event": args.ev,
        "IsConfirmed": args.ic,
        "LowestSeverity": args.ls,
        "Name": args.n,
        "Scope": args.sc
        }
    
    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 201:
        print(response.text)

    else:
        print("Notification has been created.")

def main():

    notifications_new()

if __name__ == '__main__':
    main()