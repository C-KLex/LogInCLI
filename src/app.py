""" 
This file is to create a main function for users to log-in or register, 
and the record will be put in log file. 
The data will be put in backend.csv 
"""
import datetime  # Datetime will be used to record the login time
import csv  # csv will be used to process the data in backend.csv


def main():
    """
    First check if user is logging-in or is registering
    """

    message1 = input(
        "\nLogging in or Creating Account? (Input Login or Create to continue)"
    )

    # If they are logging-in, jumpin this condition
    if message1 == "Login":
        print("\nWelcome Back, Please Enter your User Name and Password Below: \n")

        # First open the backend data
        with open("backend.csv", "r", encoding="utf-8") as record:

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
                    with open("log", "a", encoding="utf-8") as log_in_history:
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

    # If they are creating account, jumpin this condition
    elif message1 == "Create":
        # Acquire the username and password
        print("\nPlease Enter Your Information Below to Finish Your Registration.\n")
        username = input("Username(email): ")
        password = input("Password: ")

        # First check if account already exists the backend data
        with open("backend.csv", "r", encoding="utf-8") as record:
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
        with open("backend.csv", "r", encoding="utf-8") as history:
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
                with open("backend.csv", "a+", encoding="utf-8") as registor:
                    writer = csv.DictWriter(registor, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(row_first_register)

            # If it's not the first registration, just append the username and password.
            else:
                with open("backend.csv", "a+", encoding="utf-8") as registor:
                    row_later_register = {username: password}
                    writer = csv.writer(registor)
                    writer.writerows(row_later_register.items())
            print("\nRegistered Successfully!\n")

    # If the user entered something unrecognizable, print this message.
    else:
        print("Wrong instrction, please try again.")
