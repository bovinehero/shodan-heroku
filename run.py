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


def get_query_data():
    """
    Get IP target for shodan query.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a valid IPv4 String.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print('\n[+] Please enter the IP Address for Shodan to Query')
        print('[+] Data should be IPv4 format, 4 octets period/fullstop')
        print('[+] Example: 8.8.8.8\n')

        ip_str = input('[+] Enter target IP Address here:\n')

        if validate_user_input(ip_str):
            break

    return ip_str


def validate_user_input(ip_str):
    """
    Inside the try, checks if input is valid ipv4.
    Raises ValueError if not.
    """
    valid_regex = \
        "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)" \
        "{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(valid_regex, ip_str):
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
        print('[+] Placeholder to validate the format the data')
    return data


def poc():
    """ just a poc details results function """
    print("I am the PoC Function")


def main():
    """ main finction to handle the runtime """
    # poc()
    target = get_query_data()
    result = shodan_helper.ShodanAPI(
        secrets_file=shodan_helper.SHODAN_SECRETS_FILE
        ).ip_scanned(target_ip=target)
    print(json.dumps(result, indent=2))
    # input IP
    # IP validator
    # Scan selector
    # Scan validator
    # Execute Scan
    # Scan Incrementor
    # Scan Logger
    # Display Results


if __name__ == "__main__":
    print("Make yourself comfortable, Hacker. Stay a while.")
    while True:
        main()
