"""
This file contains the function for users to register.
"""

import csv  # csv will be used to process the data in backend.csv


def register():
    # Acquire the username and password
    print("\nPlease Enter Your Information Below to Finish Your Registration.\n")
    username = input("Username(email): ")
    password = input("Password: ")

    # First check if account already exists the backend data
    with open("src/backend.csv", "r", encoding="utf-8") as record:
        key1 = csv.DictReader(record)
        for row in key1:

            # If the user name is already registered, decline the registration
            if ("username", username) in row.items():
                print(
                    "\nAccount already exists, please log-in or change an user name and try again.\n"
                )
                # Not need to run further codes so just exit.
                exit()

    # If the user name is not yet registered, put their data in backend.csv
    row_first_register = [{"username": username, "password": password}]
    field_names = ["username", "password"]

    # Open the backend data file
    with open("src/backend.csv", "r", encoding="utf-8") as history:
        key2 = csv.DictReader(history)
        # If it's the first registration of this system, add column name to backend.csv
        # Then append the username and password as dictionary in backend.csv
        # This will allow the log-in part of code to examine if the password and username are right.
        length = 0
        for rows in key2:
            length += 1  # If there are more then one rows in the file,
            # it means it's not the first registration

        # This is the condition to check if it's the first registration.
        if length == 0:
            with open("src/backend.csv", "a+", encoding="utf-8") as registor:
                writer = csv.DictWriter(registor, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(row_first_register)

        # If it's not the first registration, just append the username and password.
        else:
            with open("src/backend.csv", "a+", encoding="utf-8") as registor:
                row_later_register = {username: password}
                writer = csv.writer(registor)
                writer.writerows(row_later_register.items())
        print("\nRegistered Successfully!\n")

