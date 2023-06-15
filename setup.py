"""
Summary:
    The set up before running the CLI
"""
import subprocess
import csv

HEADER = ["USERNAME", "PASSWORD"]

def setup_backend_database():

    print("********************************Setting up backend database********************************")
    user_input = input("WARNING: This action will rebuild the database!!!! (y\\n): ")

    if user_input in ["Y", "y"]:
        subprocess.run(["touch", "login_cli/backend/backend.csv"])
        with open("login_cli/backend/backend.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
            f.close()

        print("DONE SETUP DATABASE")
    elif user_input in ["N", "n"]:
        print("SKIP SETUP DATABASE")

def setup_log():
    
    print("********************************Setting up log********************************")
    user_input = input("WARNING: This action will delete the previous log!!! (y\\n): ")

    if user_input in ["Y", "y"]:
        subprocess.run(["touch", "login_cli/backend/log.txt"])

        with open("login_cli/backend/log.txt", "w") as f:
            f.write("")
            f.close()

        print("DONE SETUP LOG")

    elif user_input in ["N", "n"]:
        print("SKIP SETUP LOG")

if __name__ == '__main__':
    setup_backend_database()
    setup_log()
