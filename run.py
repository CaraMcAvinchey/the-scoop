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

# Customer Information

def user_info():
    """
    Collect the customer's first name for their order.
    """
    print("Let's get scooping!\n")
    print("Tell us your name so we can call you when your order is ready.\n")
    while True:
        name = input("Enter your name here:\n").capitalize().strip()

        end_section()

        if validate_name(name):
            print(f"Hello {name}")
            break

    return name

def validate_name(name):
    """
    Validate customer name.
    Check if the customer input numbers or characters.
    Check if their name is at least 2 characters long.
    """
    try:
        if name.isnumeric():
            raise ValueError(
                "Please input your name using letters only, not numbers.") 

        if not name.isalpha():
            raise ValueError(
                "Please input your name using letters only, not characters.")          

        if len(name) < 2:
            raise ValueError(
                "Your name needs to be at least two characters long.")

    except ValueError as e:
        print(f"{e} \nPlease try again.")
        return False

    return True   

# Program Formatting
def end_section():
    """
    Print ### to end each section.
    """
    print(" ")
    print("# "* 25)
    print(" ")

# Main Functions

def main():
    """
    Run the main code
    """
    # Welcome message
    welcome_message()
    end_section()
    #Customer Information
    user_info()

main()