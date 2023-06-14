import csv
csv_path_from_main = "login_cli/backend/backend.csv"

class Backend:

    @classmethod
    def login_validation(cls, username, password):
        return False 
    
    @classmethod
    def add_account(cls, username, password):

        with open(csv_path_from_main, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
            f.close()

    @classmethod
    def account_exist(cls, username):
        users = set()
        with open(csv_path_from_main, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
              users.add(row[0])  
            f.close()

        return username in users
        