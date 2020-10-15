import requests
import json
import argparse
import csv

file = open("config.json", "r")
data = json.load(file)
file.close()

USER_ID = data['USER_ID']
API_TOKEN = data['API_TOKEN']
API_ROOT = data['API_ROOT']
AUTH = (USER_ID, API_TOKEN)

def scans_report():

    endpoint_url = API_ROOT % "scans/report"
    parser = argparse.ArgumentParser(description='Returns the report of a scan in the specified format.')
    parser.add_argument('-cf', '-contentf', type=str, choices=['Html', 'Markdown'], help='Gets or sets the content format. This parameter can only be used for vulnerabilities XML and JSON report.')
    parser.add_argument('-er', '-exredt', type=str, choices=['true', 'false'], help='If set to true, HTTP response data will be excluded from the vulnerability detail. This parameter can only be used for vulnerabilities XML report. Default: false')
    parser.add_argument('-f', '-format', type=str, choices=['Xml', 'Csv', 'Pdf', 'Html', 'Txt', 'Json'], help='Gets or sets the report format. Crawled URLs, scanned URLs and vulnerabilities can be exported as XML, CSV or JSON. Scan detail, Owasp Top Ten 2013, PCI Compliance, HIPAA Compliance, Executive Summary and Knowledge Base reports can be exported as HTML or PDF. ModSecurity WAF Rules report can be exported as TXT.', required=True)
    parser.add_argument('-id', '-scanid', type=str, help='Gets or sets the scan identifier.', required=True)
    parser.add_argument('-t', '-type', type=str, choices=[
        'Crawled',
        'Scanned',
        'Vulnerabilities',
        'ScanDetail',
        'ModSecurityWafRules',
        'OwaspTopTen2013',
        'HIPAACompliance',
        'PCICompliance',
        'KnowledgeBase',
        'ExecutiveSummary',
        'FullScanDetail',
        'OwaspTopTen2017',
        'CustomReport',
        'ISO27001Compliance',
        'F5BigIpAsmWafRules'
    ], help='Gets or sets the report type. FullScanDetail option corresponds to "Detailed Scan Report (Including addressed issues)". ScanDetail option corresponds to "Detailed Scan Report (Excluding addressed issues)".', required=True)
    parser.add_argument('-oc', '-confirmed', type=str, choices=['true', 'false'], help='If this field set true then only the Confirmed Issues will be included to the report results. This option not valid for KnowledgeBase, Crawled, Scanned, ModSecurityWafRules, F5BigIpAsmWafRules report types. Default: null')
    parser.add_argument('-ea', '-exadis', type=str, choices=['true', 'false'], help='If this field set true then the Addressed Issues will be excluded from the report results. FullScanDetail and ScanDetail options override this field. This option not valid for KnowledgeBase, Crawled, Scanned, ModSecurityWafRules, F5BigIpAsmWafRules report types. Default: null')
    
    args = parser.parse_args()

    parameters = {
        'contentFormat': args.cf,
        'excludeResponseData': args.er, 
        'format': args.f, 
        'id': args.id,
        'type': args.t,
        'onlyConfirmedIssues': args.oc,
        'excludeAddressedIssues': args.ea
        }

    response = requests.get(endpoint_url, params=parameters, auth=AUTH)
    
    if (response.status_code == 200):

        with open('Scans_Report.csv', 'w', encoding='utf8') as wf:
            wf.write(response.text)

        print("Response: %s - %s" % (response.status_code, response.reason))
        print("The scan report is saved into the 'Scans_Report.csv' file.")

    else:
        print("Response: %s - %s" % (response.status_code, response.reason))
        print(response.text)

def main():

    scans_report()

if __name__ == '__main__':
    main()