import datetime
import subprocess
import csv
import time 

from login_cli.backend.backend import Backend, CSV_PATH_FROM_MAIN, LOG_PATH_FROM_MAIN

def create_csv():
    subprocess.run(["touch", CSV_PATH_FROM_MAIN])
    with open(CSV_PATH_FROM_MAIN, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["USERNAME", "PASSWORD"])
        writer.writerow(["foo", "bar"])
        f.close() 

def rm_csv():
    subprocess.run(["rm", CSV_PATH_FROM_MAIN])

def create_log():
    subprocess.run(["touch", LOG_PATH_FROM_MAIN])
    with open(LOG_PATH_FROM_MAIN, "w") as f:
        f.close()

def rm_log():
    subprocess.run(["rm", LOG_PATH_FROM_MAIN])

def test_login_valid():
    create_csv()
    assert Backend.login_validation("foo", "bar") == True 
    rm_csv()

def test_login_invalid():
    create_csv()
    assert Backend.login_validation("foo", "wrong password") == False
    rm_csv()

def test_acc_exist():
    create_csv()
    assert Backend.account_exist("foo") == True 
    rm_csv()

def test_acc_not_exist():
    create_csv()
    assert Backend.account_exist("wrong username") == False
    rm_csv()

def test_add_acc():
    create_csv()
    Backend.add_account("new_user", "new_password")
    assert Backend.account_exist("new_user") == True 
    assert Backend.login_validation("new_user", "new_password")
    rm_csv()

def test_return_log():
    create_log()
    row = "test row"
    with open(LOG_PATH_FROM_MAIN, "a") as f:
        f.write(row)
        f.close()
    assert Backend.return_log() == [row]
    rm_log()

def test_write_login_log():
    create_log()
    name = "foo"
    rows = 100 
    with open(LOG_PATH_FROM_MAIN, "a", newline = "") as f:
        for _ in range(rows):
            time.sleep(0.001)
            Backend.write_login_log(name)
        f.close()
    logs = Backend.return_log()
    assert len(logs) == rows 
    assert len(set(logs)) == rows
    rm_log()