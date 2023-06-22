from src.utils import reload, register, login

def main():

    usernames, passwords = reload()
    action = input("Enter 0 for register, enter 1 for login: ")

    if action == "0":
        register(usernames)
    
    elif action == "1":
        login(usernames, passwords)

    else:
        print("Wrong command. Please try again.")






