def main():
    usernames = []
    passwords = []

    with open("backend.csv", "a+", encoding="utf-8") as be:
        be.seek(0)
        res = be.readlines()
        for i in res:
            r = i.strip()
            arr = r.split(':')
            usernames.append(arr[0])
            passwords.append(arr[1])

    registered = True
    while registered:
        username = input("Please enter the username: ")
        if username in usernames:
            print("")