def main():

    import datetime
    # backend.csv storage
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

    action = input("0 for registration, 1 for login: ")
    
    if action == str(0):

        register = True
        while register:

            newname = input("Please set your username: ")
            if newname in usernames:
                print("Username exists. Please try again.")
                exit()
            else:
                while True:
                    newpwd = input("Please set your password: ")
                    if len(newpwd) >= 6:
                        repwd = input("Please reenter your password: ")
                        if newpwd == repwd:
                            print(newname, newpwd)

                            with open("src/backend.csv", "a+", encoding='utf-8') as be:
                                be.write(f'{newname}:{newpwd}\n')
                            print("Successfully registered.")

                            register = False
                            break

                        else:
                            print("Unmatched. Please reenter your password.")
                    else:
                        print("Password should be longer than 5. Please try again.")
    
    elif action == str(1):

        login = True
        while login:

            username = input("Please enter your username: ")
            if username in usernames:
                while True:
                    password = input("Please enter your password: ")
                    index = usernames.index(username)
                    
                    if password == passwords[index]:
                        print("Successfully login.")

                        with open("src/log", "a+", encoding="utf-8") as loghist:
                            time = datetime.datetime.now()
                            loghist.write(str(time)+" "+str(username)+"\n")

                        login = False
                        break
                    else:
                        print("Wrong password. Please try again.")
            else:
                print("Wrong username. Please try again.")
                break
    
    else:
        print("Wrong command. Please try again.")






