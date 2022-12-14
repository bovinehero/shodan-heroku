""" Main Script Run"""

import json
import re
import gspread
from google.oauth2.service_account import Credentials
import shodan_helper

# Google Drive Scope for project

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# testing connectivity - change to shodan data
SHEET_TITLE = "shodan"
SECRETS_FILE = "gspread_secrets.json"
CREDS = Credentials.from_service_account_file(filename=SECRETS_FILE)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open(title=SHEET_TITLE)
TARGET_LIMIT = 12
REPORT_HEADERS = [
    "Target",
    "City",
    "Region",
    "OS",
    "ShodanTags",
    "ISP",
    "Area",
    "Longitude",
    "LastUpdate",
    "Ports",
    "Latitude",
    "Hostnames",
    "Country",
    "Country",
    "Domains",
    "Orginisation"
]


def first_run_check(sheet_title="ip scans"):
    try:
        work_sheet = SHEET.worksheet(title=sheet_title)
        data = work_sheet.get_all_values()
        if data:
            pass
    except gspread.exceptions.WorksheetNotFound as err:
        print(f'[-] Missing Worksheet {err}, building...')
        clear_worksheet()
    else:
        print("[+] All recording systems ready.")
    finally:
        print("Make yourself comfortable, Hacker. Stay a while.")


def analyse_data(json_data, sheet_title="ip scans"):
    """
    Get IP target for shodan query.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a valid IPv4 String.
    The loop will repeatedly request data, until it is valid.
    """
    if json_data:
        ip = str(json_data['ip_str'])
        city = str(json_data['city'])
        region_code = str(json_data['region_code'])
        os = str(json_data['os'])
        shodan_tags = str(' '.join(json_data['tags']))
        isp = str(json_data['isp'])
        area_code = str(json_data['area_code'])
        longitude = str(json_data['longitude'])
        last_update = str(json_data['last_update'])
        ports = str(', '.join(str(i) for i in json_data['ports']))
        latitude = str(json_data['latitude'])
        hostnames = str(', '.join(json_data['hostnames']))
        country_code = str(json_data['country_code'])
        country_name = str(json_data['country_name'])
        domains = str(' '.join(json_data['domains']))
        orginisation = str(json_data['org'])

        print(f"Target: {ip}")
        print(f"City: {city}")
        print(f"Region Code: {region_code}")
        print(f"OS: {os}")
        print(f"Shodan Tags: {shodan_tags}")
        print(f"ISP: {isp}")
        print(f"Area Code: {area_code}")
        print(f"Longitude: {longitude}")
        print(f"Last Updated: {last_update}")
        print(f"Ports: {ports}")
        print(f"Latitude: {latitude}")
        print(f"Hostnames: {hostnames}")
        print(f"Country Code: {country_code}")
        print(f"Country Name: {country_name}")
        print(f"Domains: {domains}")
        print(f"Orginisation: {orginisation}")
        work_sheet = SHEET.worksheet(title=sheet_title)
        kickstart_report_sheet()
        searches = SHEET.worksheet(sheet_title).get_all_values()
        want_to_save = input('\n[+] press Y to save\n')
        if 'y' == want_to_save.lower() and len(searches[1:]) < TARGET_LIMIT:
            print('[+] Saving details to report')
            line_to_add = [
                ip,
                city,
                region_code,
                os,
                shodan_tags,
                isp,
                area_code,
                longitude,
                last_update,
                ports,
                latitude,
                hostnames,
                country_code,
                country_name,
                domains,
                orginisation
            ]
            work_sheet.append_row(line_to_add)
        elif 'y' == want_to_save.lower():
            print('[-] Oops Report Worksheet is full I cannot save!')
            print('[-] Either ask admin to increase capacity \
            or clear report data')
            print('[-] Not Saving details to report')
        else:
            print('[-] Not Saving details to report')
    else:
        pass


def get_query_data():
    """
    Get IP target for shodan query.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a valid IPv4 String.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print('\n[+] Please enter the IP Address for Shodan to Query')
        print('[+] Use help command for more info')
        ip_str = input('[+] Enter command:\n')
        if validate_user_input(ip_str):
            break
    return ip_str


def validate_user_input(ip_str):
    """
    Checks if user selected help.
    Checks if input is valid ipv4.
    Raises ValueError if not.
    """
    valid_regex = \
        "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"\
        "{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if ip_str.lower() == "help":
        tool_help()
        return False
    if ip_str.lower() == "clear report":
        clear_worksheet()
        return False
    if ip_str.lower() == "summary report":
        summary = fetch_gspread_data()
        print(json.dumps(summary, indent=2))
        return False
    elif re.search(valid_regex, ip_str):
        print('\n[+] Valid IP address')
        return True
    else:
        print(f'\n[-] You entered "{ip_str}"')
        print('[-] Invalid IP address, please input valid IPv4 address.\n')
        return False


def fetch_gspread_data(sheet_title="ip scans"):
    """ fetch all data from worksheet, default is ip scans """
    data = []
    try:
        work_sheet = SHEET.worksheet(title=sheet_title)
        data = work_sheet.get_all_values()
    except gspread.exceptions.WorksheetNotFound as err:
        print(f'[-] Unable to find worksheet {err}.')
    else:
        print(f'[+] Data Retrieved from {sheet_title}')
    finally:
        print('[+] Preparing Report')
        report = []
        for i in data[1:]:
            report.append(dict(zip(REPORT_HEADERS, i)))
    return report


def tool_help():
    """ run help text """
    print("""\n[!] Special Commands:
\n\tclear report: this will clear the exisitng data from the report.
\n\tsummary report: this will provide a basic summary of findings in JSON\n""")
    print('[!] Or enter an IP Address for Shodan to Query')
    print('\n[!] Data should be IPv4 format, 4 octets period/fullstop')
    print('[!] Example: 8.8.8.8 or 73.253.15.222\n')
    input('[!] Press any key to continue\n')


def clear_worksheet(sheet_title="ip scans"):
    """ this will clear the google sheet for a new report """
    print('\n[!] Clearing down the worksheet')
    col_count = len(REPORT_HEADERS)
    row_rount = TARGET_LIMIT+1
    try:
        kickstart_report_sheet(sheet_title=sheet_title)
    except gspread.exceptions.WorksheetNotFound as err:
        print(f'[-] Unable to find worksheet {err}')
        SHEET.add_worksheet(title=sheet_title, rows=row_rount, cols=col_count)
        kickstart_report_sheet(sheet_title=sheet_title)
    finally:
        print(f'[+] Clean worksheet {sheet_title} created.')


def kickstart_report_sheet(sheet_title="ip scans"):
    """ kickstart a new report worksheet with basic formatting """
    work_sheet = SHEET.worksheet(title=sheet_title)
    work_sheet.clear()
    work_sheet.update('1:1', [REPORT_HEADERS])
    work_sheet.format('1:1', {
        "backgroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 0.0
        },
        "horizontalAlignment": "CENTER",
        'textFormat': {
            'bold': True,
            "fontSize": 10,
            "foregroundColor": {
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                },
            }
        }
    )


def main():
    """ main finction to handle the runtime """
    target = get_query_data()
    result = shodan_helper.ShodanAPI(
        secrets_file=shodan_helper.SHODAN_SECRETS_FILE
        ).ip_scanned(target_ip=target)
    analyse_data(json_data=result)


if __name__ == "__main__":
    first_run_check()
    while True:
        main()
