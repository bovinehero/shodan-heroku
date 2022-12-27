""" Main Script Run"""

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import json
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
SHODAN_SECRETS_FILE = "secrets.json"
SHEET_TITLE = "shodan"
SECRETS_FILE = "gspread_secrets.json"
CREDS = Credentials.from_service_account_file(filename=SECRETS_FILE)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open(title=SHEET_TITLE)

ip = "8.8.8.8"


def read_json_file(json_file) -> dict:
    """ read local json file and return as dictionary """
    filename = os.path.join(json_file)
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


SHODAN_API_KEY = read_json_file(
    json_file=SHODAN_SECRETS_FILE)['SHODAN_API_KEY']


def fetch_gspread_data(sheet_title="ip scans"):
    """ fetch all data from worksheet, default is ip scans """
    data = []
    try:
        test_sheet = SHEET.worksheet(title=sheet_title)
        data = test_sheet.get_all_values()
    except gspread.exceptions.WorksheetNotFound as err:
        print(f'[!] Unable to find worksheet {err}.')
    else:
        print(f'[+] Data Retrieved from {sheet_title}')
    finally:
        return data


def poc():
    """ just a poc details results function """
    print("I am the PoC Function")


def main():
    """ main finction to handle the runtime """
    # poc()
    result = shodan_helper.ShodanAPI(secrets_file=SHODAN_SECRETS_FILE)\
        .ip_scanned(ip=ip)
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
    main()
