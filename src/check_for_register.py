import csv


def check(username):
    # First check if account already exists the backend data
    with open("src/backend.csv", "r", encoding="utf-8") as record:
        key1 = csv.DictReader(record)
        for row in key1:

            # If the user name is already registered, decline the registration
            if ("username", username) in row.items():
                return True
            else:
                return False
