import datetime
import csv

def main():
    print("***** Login System *****")
    print("Do you want to: ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    ch = int(input("Enter the number of your choice: "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    else: 
        print("Wrong choice!")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if confirm_password == password:
        with open("src/backend.csv","a") as f:
            f.write(username + ",")
            f.write(confirm_password + "\n")
        f.close()

        print("You have registered successfully!")
    else:
        print("Password does not match! \n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("src/backend.csv", "r") as backend_database:
        backend_datareader = csv.reader(backend_database)
        for row in backend_datareader:
            stored_username, stored_password = row[0],row[1]
            if username == stored_username and password == stored_password:
                print("Logged in successfully!")
                with open("src/log", "a") as log_database:
                    log_database.write(str(datetime.datetime.now()) + " " + str(username) + "\n")
                exit()
            else: 
                print("Login failed. Please re-enter username and password. \n")



    
    backend_database.close()

    
    