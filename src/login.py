"""
This file contains the function for users to login.
"""
import datetime  # Datetime will be used to record the login time
import csv  # csv will be used to process the data in backend.csv


def login():
    # Give user proper instruction
    print("\nWelcome Back, Please Enter your User Name and Password Below: \n")

    # First open the backend data
    with open("src/backend.csv", "r", encoding="utf-8") as record:

        # Acquire the username and password
        username = input("Username(email): ")
        password = input("Password: ")

        # Check if the username and password are right.
        key = csv.DictReader(record)
        for row in key:
            # If both username and password are right
            if (("username", username) in row.items()) and (
                ("password", password) in row.items()
            ):
                # If it's right pair of username and password, print this message.
                print("\nSuccessful Logged in! Welcome Back!\n")

                # Append the log-in history in log file
                with open("src/log", "a", encoding="utf-8") as log_in_history:
                    log_in_history.write(
                        str(datetime.datetime.now()) + "  " + str(username) + "\n"
                    )
                # Log-in successful, so end this program.
                exit()

            # If only username is in the backend data but not the password,
            # it means the user is entering wrong password,
            # so in this condition, we remind them to try another password.
            elif (("username", username) in row.items()) and (
                ("password", password) not in row.items()
            ):
                print("\nWrong password, please try again.\n")
                # Not need to run further codes so just exit.
                exit()

        # If it's not the above two scenario, it's a failed log-in, and they probably haven't
        # registered yet, so we print the below message.
        print(
            "\nLog-in not successful, please try again. (If not registered please register first.)\n"
        )
