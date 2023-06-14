import subprocess

def setup_backend_database():

    print("********************************Setting up backend database********************************")
    user_input = input("WARNING: This action will rebuild the database!!!! (y\\n): ")

    if user_input in ["Y", "y"]:
        subprocess.run(["touch", "login_cli/backend/backend.csv"])
        print("DONE SETUP DATABASE")
    elif user_input in ["N", "n"]:
        print("SKIP SETUP DATABASE")

def setup_log():
    
    print("********************************Setting up log********************************")
    user_input = input("WARNING: This action will delete the previous log!!! (y\\n): ")

    if user_input in ["Y", "y"]:
        subprocess.run(["touch", "log"])
        print("DONE SETUP LOG")
    elif user_input in ["N", "n"]:
        print("SKIP SETUP LOG")

if __name__ == '__main__':
    setup_backend_database()
    setup_log()
