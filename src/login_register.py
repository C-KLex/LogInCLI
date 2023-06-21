import csv
from datetime import datetime

def no_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input. Please try again.")


def register():
    while True:
        username = no_empty("Enter a username: ").strip()

        with open('src/backend.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            if any(row[0] == username for row in reader):
                print("Username already exists. Please choose a different username.")
            else:
                break
                    
    password = no_empty("Enter a password: ")
    with open('src/backend.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username,password])

    print(f"Congrats! {username}, Your Rsegistration is successful!")
    

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('src/backend.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        user_exists = False
        for row in reader:
            if row[0] == username:
                user_exists = True
                if row[1] == password:
                    print(f"Login successful, Hi {username}!")   
            
                    with open('src/log', 'a') as log_in_hist:
                        log_in_hist.write(f"{login_time} | {username}\n")
                    return 
                else:
                    print("Invalid password.")
                    return 
        if not user_exists:
            print("Username not found. Please register first.")

