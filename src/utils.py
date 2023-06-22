import datetime

# reload
def reload():

    usernames = []
    passwords = []

    with open("src/backend.csv", "a+", encoding="utf-8") as be:
        be.seek(0)
        res = be.readlines()
        for i in res:
            r = i.strip()
            arr = r.split(':')
            usernames.append(arr[0])
            passwords.append(arr[1])

    return usernames, passwords

# register
def register(usernames):

    newname = input("Please set your username: ")
    if newname in usernames:
        print("Username exists. Please try again.")
        exit()

    newpwd = input("Please set your password: ")
    if len(newpwd) < 6:
        print("Password should be longer than 5. Please try again.")

    repwd = input("Please reenter your password: ")
    if newpwd != repwd:
        print("Unmatched. Please reenter your password.")

    with open("src/backend.csv", "a+", encoding='utf-8') as be:
        be.write(f'{newname}:{newpwd}\n')
        
    print("Successfully registered.")
    exit()



# login
def login(usernames, passwords):

    username = input("Please enter your username: ")
    if username in usernames:
        password = input("Please enter your password: ")
        index = usernames.index(username)
        
        if password == passwords[index]:
            print("Successfully login.")

            with open("src/log", "a+", encoding="utf-8") as loghist:
                time = datetime.datetime.now()
                loghist.write(str(time)+" "+str(username)+"\n")
            exit()
        else:
            print("Wrong password. Please try again.")
    else:
        print("Wrong username. Please try again.")