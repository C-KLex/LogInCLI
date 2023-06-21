"""
This file contains the function for users to register.
"""

import csv


def register():
    print("\nPlease Enter Your Information Below to Finish Your Registration.\n")
    username = input("Username(email): ")
    password = input("Password: ")

    # First check if account already exists the backend data
    with open("src/backend.csv", "r", encoding="utf-8") as record:
        key1 = csv.DictReader(record)
        for row in key1:

            # If the user name is already registered, decline the registration
            if ("username", username) in row.items():
                return "\nAccount already exists, please log-in or change an user name and try again.\n"

    # If the user name is not yet registered, put their data in backend.csv
    row_first_register = [{"username": username, "password": password}]
    field_names = ["username", "password"]

    with open("src/backend.csv", "r", encoding="utf-8") as history:
        key2 = csv.DictReader(history)
        length = 0
        for rows in key2:
            length += 1  # If there are more then one rows in the file,
            # it means it's not the first registration

        # Check if it's the first registration.
        # If it's the first registration of this system, add column name to backend.csv
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
        return "\nRegistered Successfully!\n"

