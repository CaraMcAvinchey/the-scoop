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

# Welcome Message

def welcome_message():
    """
    Welcome the user to The Scoop.
    Introduce the service.
    """
    print("Welcome to The Scoop!\n")
    print("Enjoy a scoop (or two!) of ice cream with us.")

class IceCreamOrder:
    """
    A class used to represent The Scoop customer
    ...
    Attributes
    -----------
    user = str
        The customer's first name
    items_in_order = list
        The items a customer ordered 
    order_no = str
        An order number for the customer 
    total_price = number
        The total price of the order placed        
    Methods
    --------
    write_order_to_sheet
        Records the order placed in the spreadsheet 
    print_receipt
        Prints the order on the screen for the customer
    user_info
        Collects the first name from the customer  
    scoop_options
        Displays the menu for the customer to order from  
    repeat_order
        Allows the customer to order again        
    """

    def __init__(self):
        self.user = self.user_info()
        self.items_in_order = []
        self.order_no = ''
        self.total_price = 0
        #self.items_in_order[1, 2, 3, 3, 3, 3]

    def user_info(self):
        """
        Collect the customer's first name for their order.
        """
        print("Let's get scooping!\n")
        print("Tell us your name so we can call you when your order is ready.\n")
        while True:
            name = input("Enter your name here:\n").capitalize().strip()
            end_section()

            if validate_name(name):
                print(f"Hi {name}!\n")
                self.scoop_options()
                break

        return name

    def scoop_options(self):
        """
        Display the number of scoops to order.
        Return the answer.
        """
        print("How many scoops would you like?")
        print("1 - 1 scoop")
        print("2 - 2 scoops")
        print("3 - 3 scoops\n")
        scoop_option = input("Enter your answer here:\n").upper().strip()

        end_section()
        self.repeat_order()

        # validate order
        while scoop_option not in ("1", "2", "3"):
            print("1 - 1 scoop")
            print("2 - 2 scoops")
            print("3 - 3 scoops")
            scoop_option = input("Enter your answer here:\n").upper().strip()
            end_section()
        self.items_in_order.append(scoop_option)
        print("\nYour order has been added!")

        return scoop_option

    def write_order_to_sheet(self):
        """
        Record the order in spreadsheet.
        """
        singles = self.items_in_order.count("1")
        doubles = self.items_in_order.count("2")
        triples = self.items_in_order.count("3")
        total_price = 0.00

        sales_worksheet = select_worksheet("sales")
        one_scoop_column = sales_worksheet.col_values(1)
        two_scoop_column = sales_worksheet.col_values(2)
        three_scoop_column = sales_worksheet.col_values(3)
        sales = sales_worksheet.get_all_values()
        total_price = 0

        # get order by adding +1 to previous entry on sheet and add user's name

        if singles > 0:
            # write to the next empty row the number of singles in the right column (append to spreadsheet)
            total_price += singles*1.5
        if doubles > 0:
            # write to the next empty row the number of doubles in the right column (append to spreadsheet)
            total_price += doubles*2.5
        if triples > 0:
            # write to the next empty row the number of triples in the right column (append to spreadsheet)
            total_price += triples*2.5

        self.order_no = spreadheet_value
        self.total_price = total_price
        self.print_reciept(singles, doubles, triples)

    def print_reciept(self, singles, doubles, triples):
        """
        Print order on the screen for the customer
        """
        if singles > 0:
            # write to the next empty row (append to spreadsheet)
            print(f"Single scoop:   {singles}   = ${1.50 * singles}")
        if doubles > 0:
            print(f"Double scoop:  {doubles}    = ${2.50 * doubles}")
        if triples > 0:
            print(f"Triple scoop:  {triples}    = ${3.50 * triples}")

    def repeat_order(self):
        """
        Allow customer to order another ice cream.
        """
        print("Would you like to order another ice cream?")
        print("1 - Yes")
        print("2 - No\n")
        repeat_order = input("Enter your answer here:\n").upper().strip()

        end_section()

        if repeat_order == "1":
            self.scoop_options()

        elif repeat_order == "2":
            print("\nLet's get your order ready...\n")
            order_complete()        


def validate_name(name):
    """
    Validate customers name.
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

#DELETE THIS FUNCTION, NOT NEEDED ANYMORE
def order_complete():
    """
    Adds sales data to the worksheet.
    Informs customer that their order is done.
    """
    print("Sending your order to our scoopers...")
    # Same function as used on the love_sandwiches walk through project
    # by Code Institute
    worksheet_to_update = SHEET.worksheet('sales')
    worksheet_to_update.append_row(data)

    print("Your order is complete!")

def goodbye_message():
    """
    Let the customer know to pick up their order.
    End the ordering process.
    """
    print("Please show your order number to our scoopers.")
    print("Enjoy your ice cream!")
    print("Hope to see you again soon!")

# Program Formatting

def end_section():
    """
    Print ### to end each section.
    """
    print(" ")
    print("# " * 25)
    print(" ")

# Main Functions

def main():
    """
    Run the main code.
    """
    # Welcome message
    welcome_message()
    end_section()
    # Customer Information
    icecream = IceCreamOrder()
    icecream.scoop_options()
    goodbye_message()

main()
