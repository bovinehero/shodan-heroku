""" Main Script Run"""

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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

# Temp vars for testing
IP = "8.8.8.8"


def analyse_data(json_data):
    """
    Get IP target for shodan query.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a valid IPv4 String.
    The loop will repeatedly request data, until it is valid.
    """
    print(f"City: {json_data['city']}")
    print(f"Region Code: {json_data['region_code']}")
    print(f"OS: {json_data['os']}")
    print(f"Shodan Tags: {' '.join(json_data['tags'])}")
    print(f"ISP: {json_data['isp']}")
    print(f"Area Code: {json_data['area_code']}")
    print(f"Longitude: {json_data['longitude']}")
    print(f"Last Updated: {json_data['last_update']}")
    print(f"Ports: {' '.join(str(i) for i in json_data['ports'])}")
    print(f"Latitude: {json_data['latitude']}")
    print(f"Hostnames: {' '.join(json_data['hostnames'])}")
    print(f"Country Code: {json_data['country_code']}")
    print(f"Country Name: {json_data['country_name']}")
    print(f"Domains: {' '.join(json_data['domains'])}")
    print(f"Orginisation: {json_data['org']}")


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
        "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)" \
        "{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if ip_str.lower() == "help":
        tool_help()
        return False
    if ip_str.lower() == "clear report":
        clear_worksheet()
        return False
    if ip_str.lower() == "summary report":
        fetch_gspread_data()
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
        test_sheet = SHEET.worksheet(title=sheet_title)
        data = test_sheet.get_all_values()
    except gspread.exceptions.WorksheetNotFound as err:
        print(f'[-] Unable to find worksheet {err}.')
    else:
        print(f'[+] Data Retrieved from {sheet_title}')
    finally:
        print('[+] Placeholder to allow validation of the data')
    return data


def tool_help():
    """ run help text """
    print("""\n[!] Special Commands:
\n\t clear report: this will clear the exisitng data from the report.
\n\t summary report: this will provide a basic summary of findings\n""")
    print('[!] Or enter an IP Address for Shodan to Query')
    print('\n[!] Data should be IPv4 format, 4 octets period/fullstop')
    print('[!] Example: 8.8.8.8 or 73.253.15.222\n')
    input('[!] Press any key to continue\n')


def clear_worksheet():
    """ this will clear the google sheet for a new report """
    print('\n[!] Placeholder to clear the worksheet')


def main():
    """ main finction to handle the runtime """
    target = get_query_data()
    result = shodan_helper.ShodanAPI(
        secrets_file=shodan_helper.SHODAN_SECRETS_FILE
        ).ip_scanned(target_ip=target)
    analyse_data(json_data=result)
    # print(json.dumps(result['data'], indent=2))


if __name__ == "__main__":
    print("Make yourself comfortable, Hacker. Stay a while.")
    while True:
        main()
