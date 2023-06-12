
def legit(username, password): 
    return True 

def login():

    username = input("Enter username: \n")
    password = input("Enter password: \n")

    if legit(username, password):
        print("SUCCESSFUL LOGIN\n")
    elif not legit(username, password):
        print("INCORRECT CREDENTIALS\n")

def register():
    print("HI Registering...\n")

def main():

    run = True 

    while run:

        menu = input("1 for login, 2 for register, 3 for stop: \n")

        # login
        if menu == "1":
            login()


        elif menu == "2":
            register()
        
        elif menu == "3":
            print("STOP THE PROGRAM")
            run = False
        

