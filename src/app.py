""" 
This file is to create a main function for users to log-in or register, 
and the record will be put in log file. 
The data will be put in backend.csv 
"""
from src.login import login
from src.register import register


def main():
    """
    First check if user is logging-in or is registering
    """
    print(
        "\nWelcome to Jordan CLI :) , please choose the below actions to start your journey!"
    )

    message1 = input(
        "\nLogging in or Creating Account? (Input Login or Create to continue): "
    )

    # If they are logging-in, jumpin this condition
    if message1 == "Login":
        # Call login function
        login()

    # If they are creating account, jumpin this condition
    elif message1 == "Create":
        # Call register function
        register()

    # If the user entered something unrecognizable, print this message.
    else:
        print("\nWrong instrction, please try again.\n")
