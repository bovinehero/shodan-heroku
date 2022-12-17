# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import shodan
import gspread
from google.oauth2.service_account import Credentials

""" Google Drive Scope for project """
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# testing connectivity - change to shodan data
SHEET_TITLE = "love_sandwiches"
SECRETS_FILE = "secrets.json"
CREDS = Credentials.from_service_account_file(filename=SECRETS_FILE)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open(title=SHEET_TITLE)


def fetch_gspread_data(sheet_title="sales"):
    """ fetch all data from worksheet """
    test_sheet = SHEET.worksheet(title=sheet_title)
    data = test_sheet.get_all_values()
    print(data)


def poc():
    """ just a poc function """
    fetch_gspread_data()
    pass
    # change this to ENVs or getpass.getpass
    # SHODAN_API_KEY = input('Enter your Shodan API Key: ')
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