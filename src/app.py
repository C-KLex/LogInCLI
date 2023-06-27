""" 
This file is to create a main function for users to log-in or register, 
and the record will be put in log file. 
The data will be put in backend.csv 
"""
from src.login import login
from src.register import register


def main():
    """
    First check if user is logging-in or is registering, and call coresponding functions
    """
    print(
        "\nWelcome to Jordan CLI :) , please choose the below actions to start your journey!"
    )

    message1 = input(
        "\nLogging in or Creating Account? (Input Login or Create to continue): "
    )

    if message1 == "Login":
        print(login())
    elif message1 == "Create":
        print(register())
    else:
        print("\nWrong instrction, please try again.\n")
