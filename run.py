""" Main Script Run"""

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import shodan
import os
import json
import gspread
from google.oauth2.service_account import Credentials

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

def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

SHODAN_API_KEY = read_secrets()['SHODAN_API_KEY']

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


def scan_me(ip="8.8.8.8"):
    """ poc scan me to test heroku deploy """
    api = shodan.Shodan(SHODAN_API_KEY)
    info = api.host(ip)
    print(info)



def poc():
    """ just a poc function """
    ip = input("Please enter IP for target:\n")
    fetch_gspread_data()
    scan_me(ip)
    # change this to ENVs or getpass.getpass
    # api = shodan.Shodan(SHODAN_API_KEY)
    # info = api.host('8.8.8.8')
    # print(info)


def main():
    """ main finction to handle the runtime """
    poc()

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
