import gspread
from google.oauth2.service_account import Credentials
import random

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
    user_info
        Asks for the name of the customer
    scoop_options
        Displays the menu for the customer to order
    repeat_order
        Allows the customer to order again
    order_complete
        Records the order placed in the spreadsheet
    print_receipt
        Prints the order on the screen for the customer
    order_number
        Prints a number for customer order
    """

    def __init__(self):
        self.items_in_order = []
        self.user = self.user_info()
        self.order_no = ''
        self.total_price = 0

    def user_info(self):
        """
        Collect the customer's first name for their order.
        """
        print("Let's get scooping!\n")
        print("What's your name?\n")
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
        scoop_option = input("Enter your answer here:\n").strip()

        end_section()

        # validate customer order
        while scoop_option not in ("1", "2", "3"):
            print("How many scoops would you like?")
            print("1 - 1 scoop")
            print("2 - 2 scoops")
            print("3 - 3 scoops")
            scoop_option = input("Enter your answer here:\n").strip()
            end_section()
        self.items_in_order.append(scoop_option)

        self.repeat_order()

        return scoop_option

    def order_complete(self):
        """
        Adds sales data to the worksheet.
        Informs customer that their order is done.
        """
        singles = self.items_in_order.count("1")
        doubles = self.items_in_order.count("2")
        triples = self.items_in_order.count("3")

        worksheet_to_update = SHEET.worksheet('sales')
        one_scoop_column = worksheet_to_update.col_values(1)
        two_scoop_column = worksheet_to_update.col_values(2)
        three_scoop_column = worksheet_to_update.col_values(3)

        if singles > 0:
            one_scoop_column.append(singles)
        if doubles > 0:
            two_scoop_column.append(doubles)
        if triples > 0:
            three_scoop_column.append(triples)

        worksheet_to_update.append_row(self.items_in_order)

        print("\nYour order is with our scoopers!")
        self.print_receipt(singles, doubles, triples)

    def print_receipt(self, singles, doubles, triples):
        """
        Print order for the user with a total price.
        """
        if singles > 0:
            singles_price = "${:,.2f}".format(1.5 * singles)
            print(f"Single scoop: {singles} = {singles_price}")

        if doubles > 0:
            doubles_price = "${:,.2f}".format(2.5 * doubles)
            print(f"Double scoop: {doubles} = {doubles_price}")

        if triples > 0:
            triples_price = "${:,.2f}".format(3.5 * triples)
            print(f"Triple scoop: {triples} = {triples_price}")

        price = (1.50 * singles) + (2.50 * doubles) + (3.50 * triples)
        total_price = "${:,.2f}".format(price)

        print(f"Total: {total_price}")

        self.order_number()

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

        if repeat_order == "2":
            print("\nLet's get your order ready...\n")
            self.order_complete()
            
        if repeat_order not in ("1", "2"):
            print("Enter the number 1 or 2 please!")
            self.repeat_order()

    def order_number(self):
        """
        Generates an order number for the customer.
        """
        print(' ')
        order_no = random.randint(1, 100)
        print(f"Your order number is {order_no}")


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


def goodbye_message():
    """
    Let the customer know to pick up their order.
    End the ordering process.
    """
    end_section()

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
    # icecream.scoop_options()
    goodbye_message()


main()
