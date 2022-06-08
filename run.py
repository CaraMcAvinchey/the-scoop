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

# Customer Login/Registration

def login_or_register():
    """
    Check if the user wants to log in or register.
    Return the answer.
    """
    print("Let's get scooping:\n")
    print("Please select the following options. I'd like to...")
    print("1 - LOGIN")
    print("2 - REGISTER")
    answer = input("Enter your answer here:\n").strip()

    end_section()
    # Validate users input as correct
    while answer not in ("1", "2"):
        print("Please choose either option 1 or 2.")
        answer = input("Enter your answer here:\n").strip()
    return answer

# Program Formatting
def end_section():
    """
    Print ### to end each section.
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

    #Login/Registration 
    login_or_register()

main()