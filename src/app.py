from src.login_register import login, register

def main():
    while True:
        choice = input("Please Enter Numbers: Register(1), Login(2), or Exit(3)? ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            exit()
        else:
            print("Invalid choice. Please try again.")