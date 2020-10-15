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

def scans_verifyformauth():

    endpoint_url = API_ROOT % "scans/verifyformauth"
    parser = argparse.ArgumentParser(description='Verifies the specified form authentication settings.')

    parser.add_argument('-lu', '-loginurl', type=str, help='Gets or sets the login form URL', required=True)
    parser.add_argument('-pw', '-password', type=str, help='Gets or sets the password', required=True)
    parser.add_argument('-tu', '-targeturl', type=str, help='Gets or sets the scan target URL', required=True)
    parser.add_argument('-un', '-username', type=str, help='Gets or sets the user name', required=True)

    # OtpSettings

    parser.add_argument('-ot', '-otptype', type=str, choices=['Totp', 'Hotp'], help='Gets or sets OtpType')
    parser.add_argument('-sk', '-key', type=str, help='Gets or sets secret key')
    parser.add_argument('-dg', '-digit', type=str, choices=['OtpDigit6', 'OtpDigit7', 'OtpDigit8'], help='Gets or sets digit')
    parser.add_argument('-p', '-period', type=int, help='Gets or sets period (seconds)')
    parser.add_argument('-al', '-algorithm', type=str, choices=['Sha1', 'Sha256', 'Sha512'], help='Gets or sets hash algorithm')

    args = parser.parse_args()
    
    if (args.ot or args.sk or args.dg or args.p or args.al):
        
        OtpSettings = {
            'OtpType': args.ot,
            'SecretKey': args.sk,
            'Digit': args.dg,
            'Period': args.p,
            'Algorithm': args.al
        }

        json_object = {
        "OtpSettings": OtpSettings,
        "LoginFormUrl": args.lu,
        "Password": args.pw,
        "ScanTargetUrl": args.tu,
        "Username": args.un
        }

    else:
    
        json_object = {
            "LoginFormUrl": args.lu,
            "Password": args.pw,
            "ScanTargetUrl": args.tu,
            "Username": args.un
            }
    
    response = requests.post(endpoint_url, json=json_object, auth=AUTH)
    
    print("Response: %s - %s" % (response.status_code, response.reason))
    
    if response.status_code != 200:
        print(response.text)

    else:
        print("Form Authentication settings have been verified.")

def main():

    scans_verifyformauth()

if __name__ == '__main__':
    main()