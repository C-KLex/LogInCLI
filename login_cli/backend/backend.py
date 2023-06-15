"""
Summary:
    The backend of LogIn_CLI
"""

import csv
from datetime import datetime

CSV_PATH_FROM_MAIN = "login_cli/backend/backend.csv"
LOG_PATH_FROM_MAIN = "login_cli/backend/log.txt"

class Backend:

    @classmethod
    def login_validation(cls, username: str, password: str) -> bool():
        """
        Summary:
            Check if the 'password' is matched with the database of given 'username'
        """
        
        with open(CSV_PATH_FROM_MAIN, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                uname = row[0]
                pword = row[1]
                if uname == username:
                    break 
            f.close()

        return password == pword  
    
    @classmethod
    def add_account(cls, username: str, password: str):
        """
        Summary: 
            Add ['username', 'password'] to the database
        
        """

        with open(CSV_PATH_FROM_MAIN, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
            f.close()

        return 

    @classmethod
    def account_exist(cls, username: str) -> bool():
        """
        Summary:
            Check if 'username' has already existed in the database
        
        """

        users = set()
        with open(CSV_PATH_FROM_MAIN, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
              users.add(row[0])  
            f.close()

        return username in users
    
    @classmethod
    def write_login_log(cls, username: str):
        """
        Summary:
            Write a line of log to the log.txt file
        """

        with open(LOG_PATH_FROM_MAIN, "a") as f:
            
            log = str(datetime.now()) + " | " + username + "\n"
            f.write(log)
            f.close()

    @classmethod
    def return_log(cls) -> list():
        """
        Summary:
            Return all logs in a list
        """
        lines = [] 

        with open(LOG_PATH_FROM_MAIN, "r") as f:
            for line in f:
                lines.append(line)
        
        return lines
        