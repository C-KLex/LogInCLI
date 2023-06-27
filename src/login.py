"""
This file contains the function for users to login.
"""
import datetime
import csv


def login():
    print("\nWelcome Back, Please Enter your User Name and Password Below: \n")

    with open("src/backend.csv", "r", encoding="utf-8") as record:
        username = input("Username(email): ")
        password = input("Password: ")

        # Check if the username and password are right.
        key = csv.DictReader(record)
        for row in key:
            # If both username and password are right
            if (("username", username) in row.items()) and (
                ("password", password) in row.items()
            ):

                # Append the log-in history in log file
                with open("src/log", "a", encoding="utf-8") as log_in_history:
                    log_in_history.write(
                        str(datetime.datetime.now()) + "  " + str(username) + "\n"
                    )
                return "\nSuccessful Logged in! Welcome Back!\n"

            # If only username is in the backend data but not the password,
            # it means the user is entering wrong password,
            # so in this condition, we remind them to try another password.
            elif (("username", username) in row.items()) and (
                ("password", password) not in row.items()
            ):
                return "\nWrong password, please try again.\n"

        # If it's not the above two scenario, it's a failed log-in, and they probably haven't
        # registered yet, so we print the below message.
        return "\nLog-in not successful, please try again. (If not registered please register first.)\n"
