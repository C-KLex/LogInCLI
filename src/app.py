import csv
from datetime import datetime

def register():

    while True:
        username = input("Enter a username: ").strip()
        if username:
            break
        print("Invalid username. Please try again.")
        
    with open('src/backend.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username:
                print("Username already exists. Please choose a different username.")
                return 

    while True:
        password = input("Enter a password: ").strip()
        if password:
            break
        print("Invalid password. Please try again.")
    
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
        for row in reader:
            if row[0] == username and row[1] == password:
                print(f"Login successful, Hi {username}!")   
            
                with open('src/log', 'a') as log_in_hist:
                    log_in_hist.write(f"{login_time} | {username}\n")

                return 
    print("Invalid username or password.")
    

def main():

    choice = input("Register(1),  Login(2) or Exit(3) ?: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        exit()
    else:
        print("Invalid. Please type again.")
        