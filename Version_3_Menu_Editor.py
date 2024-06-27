##########################################################
# Author : Kyle Stranick                                 #
# Class : ITN160                                         #
# Class Section : 401                                    #
# Date : 10/27/2023                                      #
# Assignment 8: Menu Editor Program                      #
# Version : 3.1                                          #
##########################################################

###################
#Syntax References:
###################
# code academy go APP
# Cannon, Jason. (2016). Python Succinctly., Syncfusion Inc.
# Gupta, Anubhav. Slither into Python. (2021?)
# Murach, Mike. (2021). Murach's Python Programming (2nd Ed.), Mike Murach & Associates, Inc.
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# https://www.tutorialspoint.com/python/python_if_else.htm
# https://www.tutorialspoint.com/python/python_functions.htm
# https://www.w3schools.com/python/
# https://www.pluralsight.com  I have a subscription
# https://www.w3schools.com/python/python_dictionaries.asp
# https://initialcommit.com/blog/python-isalpha-string-method
# https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
# https://www.geeksforgeeks.org/python-test-if-string-contains-alphabets-and-spaces/
# https://www.geeksforgeeks.org/find-average-list-python/
# https://code-basics.com/languages/python/lessons/magic-numbers
# https://wiki.python.org/moin/HandlingExceptions
# https://wiki.python.org/moin/ForLoop
# https://wiki.python.org/moin/WhileLoop
# https://docs.python.org/3/tutorial/datastructures.html
# https://guicommits.com/organize-python-code-like-a-pro/
# https://docs.python-guide.org/writing/structure/
# https://www.askpython.com/python/examples/generate-random-colors#:~:text=Using%20the%20random%20module&text=We%20can%20implement%20it%20to%20generate%20random%20colors.&text=Here%20we%20have%20created%20a,returns%20them%20as%20a%20tuple.
# https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-game <- implement??
# https://stackoverflow.com/questions/63769198/giving-one-hint-for-each-of-the-tries-guessing-number-game
# https://realpython.com/python-raise-exception/
# https://realpython.com/python-raise-exception/#choosing-the-exception-to-raise-built-in-vs-custom
# https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string
# https://dbader.org/blog/meaning-of-underscores-in-python
# https://www.programiz.com/python-programming/csv#google_vignette
# https://www.w3schools.com/python/ref_keyword_del.asp#:~:text=Definition%20and%20Usage,parts%20of%20a%20list%20etc.
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/functions.html
# https://www.geeksforgeeks.org/file-flush-method-in-python/
# https://docs.python.org/3/library/getpass.html
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
# https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered#:~:text=this%20can%20be%20resolved%20by,link%20to%20python's%20Lib%20folder.&text=this%20will%20add%20*%20to%20your%20password%20inputs.
# https://stackoverflow.com/questions/9202224/getting-a-hidden-password-input
# https://www.youtube.com/watch?v=dR_cDapPWyY
# https://stackoverflow.com/questions/69301274/how-to-make-sign-up-and-login-program-in-python
# https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string
#
################
# Version Notes:
################
# Version 1.0: base program began with simple I/O and print  functions
# Version 1.1: using filenotfounderror to return empty list
# Version 1.2: menu would not load needed to add comma between menu.csv and r
# Version 1.3: edit_item function not working needed to add int to index_function, will not display menu after
# subsequent entries moving display_menu to inside while loop
# Version 1.4: in display_menu fixed price display by adding item parameter to for loop
# Version 2.0: added asking save function to add_item, edit_item and delete_item to cover for potential data loss
# Version 2.1: added exit functions to to the choices
# Version 2.2: created get_item_input function to hold inputs
# Version 2.3: added username and password function to program to mimic realworld applications
# Version 2.4: moved choices to separate function
# Version 2.5: added try/except to edit_item to catch for invalid indexes
# Version 3.1: imported getpass to hide password input


from getpass import getpass  # only runs properly in terminal
import csv  # used for reading and writing CSV files.
from colorama import Fore, init  # coloring terminal text output
init(autoreset=True)  # used to initialize colorama for terminal color output and automatically reset after use

# login information
USERS = {"manager": "restaurant1"}  # dictionary storing usernames as keys and passwords as values


def main():
    """
    primary function that loops through various menu options
    """
    menu = load_menu()
    print(f"\nRestaurant Menu Editor")
    while True:
        display_menu(menu)
        display_choice()
        choice = input("Choose Option (1-4): ")
        if choice == "1":
            add_item(menu)
        elif choice == "2":
            edit_item(menu)
        elif choice == "3":
            delete_item(menu)
        elif choice == "4":
            save_menu(menu)
            break
        else:
            print(Fore.RED + f"Invalid Choice Select Again")


def get_user():
    """
    Prompt user for a username.

    Returns:
        str: Username provided by the user.
    """
    return input("Enter Username: ")


def get_password(username):
    """
    Prompt for the password associated with a username.

    Parameters:
        username (str): Username for which the password is to be input.

    Returns:
        str: Password provided by the user.
    """
    return getpass(f"Enter Password For {username}: ")


def login():
    """
    Handles user login.

    Prompts the user for username and password. Will keep prompting if credentials are invalid.

    Returns:
        bool: True if login successful, keeps looping otherwise.

    before the main function begins, user is prompted for username and password and will loop if incorrect. Keyerror
    is raised when incorrect username and/or password is entered
    if true the function will break and enter main()
    """
    while True:
        username = get_user()
        password = get_password(username)

        try:
            if USERS[username] == password:
                print(f"Login Successful")
                return True  # will break loop is login is correct
            else:
                raise KeyError
        except KeyError:
            print(Fore.RED + f"Invalid Login Credentials. Re-Enter Correct Credentials.")


def display_choice():
    """Displays menu options to the user."""
    print(f"\nOptions:")
    print(f"1. Add Item")
    print(f"2. Edit Item")
    print(f"3. Delete Item")
    print(f"4. Exit\n")


def display_menu(menu):
    """
    displays all items in the current menu with their assigned index number
    Parameters:
        menu (list): List of menu items.
    """
    print(f"\nMenu Items")
    for index_number, item in enumerate(menu):  # funtion to loop over the iterable menu and indexes them
        print(f"{index_number}. {item['Name']}: {item['Description']} - ${item['Price']}")


def response_prompt(prompt):
    """
        Query the user to decide whether to continue with the program.

    Parameters:
    - prompt (str): A string to display when requesting input from the user.

    Returns:
    - bool: True if the user enters 'Y', False if the user enters 'N'.

    The function continuously prompts the user until a valid input (Y/N) is provided,
    ensuring that the program only proceeds with a clear affirmative or negative from the user.
     Gets a yes/no response from the user based on the provided prompt

    """
    while True:
        response = input(prompt).upper()
        if response in ["Y", "N"]:
            return response == "Y"
        print(Fore.RED + f"\nInvalid input. Please enter Y or N.\n")


def load_menu():
    """
    Load the restaurant menu from 'menu.csv'.

    Returns:
        list: List of menu items. Returns an empty list if file not found.

    try block checks for the existence of menu.csv. If not the try/except block catches the filenotfounderror
    and creates the file if not
    the reader returns a reader object to iterate over lines and maps it to a dict
    """
    try:
        with open("menu.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def save_menu(menu):
    """
    Save the menu to 'menu.csv'.

    Parameters:
        menu (list): List of menu items to be saved.
    this function opens the menu.csv and allows it to be overwritten. Create an object which operates like a regular
    writer but maps dictionaries onto output rows. In the writer variable the menu will be written into a dict with
    headers established by the column variable.
    """
    with open("menu.csv", "w", newline='') as file:
        columns = ["Name", "Description", "Price"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(menu)


def get_item_input():  # look up multiple return version 2
    """
    Prompt the user for menu item details.

    Returns:
        dict: Dictionary containing name, description, and price of the item.
              Returns None if user decides to exit input.
    this function allows the user to input menu items. Entered items will evaluate to true if entered correctly and
    stored in a dict for later use.
    """
    name = input(f"\nEnter item name (or 'exit' to stop): ")
    if name.lower() == "exit":  # will evaluate to True if exit is entered in either upper or lowercase
        return None  # returns None value to be called later in add_item and edit_item
    description = input(f"Enter item description (or 'exit' to stop): ")[:50]
    if description.lower() == "exit":
        return None  # returns that
    while True:  # loops until proper float is input
        price_input = input(f"Enter price (or 'exit' to stop): ")
        if price_input.lower() == "exit":
            return None
        try:  # this block converts strings into floats and returns ValueError if it cannot
            price = float(price_input)
            break
        except ValueError:
            print(Fore.RED + f"Invalid price. Please enter a valid decimal number or 'exit'.")
    return {'Name': name, 'Description': description, 'Price': str(price)}


def save_changes(menu):
    """Prompt user to save changes and save if confirmed."""
    if response_prompt(f"Would you like to save changes?(y/n): "):
        print(Fore.RED + f"Changes Saved")
        save_menu(menu)


def add_item(menu):
    """
    Allow users to add items to the menu.

    Parameters:
        menu (list): List of current menu items.

    this looped function will append menu inputs to the menu and will use stored None to exit inputs it exit it typed
    only after items are added will the function prompt users to keep entering items or to save newly added items.
    if the user decides not to save then the program will break without saving.
    """
    while True:
        item = get_item_input()
        if item is None:
            print(f"Input Aborted.")
            break
        menu.append(item)

        if not response_prompt(f"\nWould you like to keep entering menu items?(y/n): "):
            save_changes(menu)
            break


def edit_item(menu):
    """
    Allow users to edit items in the menu.

    Parameters:
        menu (list): List of current menu items.
    this function allows the user to edit a selected index if the user selects an index outside the bounds
    an error is raised to gracefully catch this. If user enters none then the function is exited.
    """
    while True:  # figure out how to select each individual detail
        display_menu(menu)
        try:  # added ver 2 needed to catch valueerror
            index_number = int(input(f"Which item would you like to change?: "))
            if index_number < 0 or index_number >= len(menu):  # added to stop index error
                raise ValueError()
            item = get_item_input()
            if item is None:
                print(f"Edit Aborted")
                break

            menu[index_number] = item
            if not response_prompt(f"Would you like to keep editing menu items?(y/n): "):
                save_changes(menu)
                break
        except ValueError:
            print(Fore.RED + f"Invalid Entry Enter Valid Index")


def delete_item(menu):
    """
    Allow users to delete items from the menu.

    Parameters:
        menu (list): List of current menu items.
    """
    while True:
        display_menu(menu)
        index_input = (input(f"\nSelect item number to delete: "))

        if index_input.lower() == "exit":
            break
        try:
            index_number = int(index_input)
            if index_number < 0 or index_number >= len(menu):  # added to stop index error
                raise ValueError()
            item_name = menu[index_number]["Name"]
            if response_prompt(f"Are you sure you want to delete {item_name}?(y/n): "):
                del menu[index_number]
                print(Fore.YELLOW + f"{item_name} Deleted")
                save_changes(menu)
                break
        except ValueError:
            print(Fore.RED + f"Enter valid item number or 'exit'.")


if __name__ == "__main__":
    if login():  # added to set up login before main program if true will run the main program
        main()
