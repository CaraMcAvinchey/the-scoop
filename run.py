import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ice_cream')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

# Welcome Function

def welcome_message():
    """
    Welcome the user to The Scoop.
    Introduce the service.
    """
    print("Welcome to The Scoop!")
    print("Enjoy a scoop (or two!) of ice cream with us.")

# Program Formatting
def end_section():
    """
    Print a ### to end each section.
    """
    print(" ")
    print("# "* 25)
    print(" ")

# Main Function

def main():
    """
    Run the main code
    """
    # Welcome message
    welcome_message()
    end_section()

main()