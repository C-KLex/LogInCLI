# 🔐LogInCLI

## 📄Summary

Design and develop a simple login CLI (Command Line Interface) application. The CLI provides `User Register` and `User Login`. Besides the two main services, the CLI also outputs a log file to track the login record.

First, branch out your branch from the latest `main` branch. Second, develop the CLI. Finally, just stay in your branch and never merge back to the `main`.

## 📚Design Needs

* `User Register`

    The CLI will provide a User to register an account, and the CLI will store the login information in the backend database. For the database, you can simply create a `.csv` file to store the user account information.

* `User Login`

    The CLI will access the backend database to authenticate the user. If log in successfully, the CLI will write the login log into the log file.

    For example,

        DataTime1 | User1
        DataTime2 | User2

* Log File

    It stores the login history if the user's login is successful.

## 🏨Project Structure Template Recommendations

* The template structure

    I draft the struct based on my personal preference, it's all good for you to use your template. You will freely delete, edit, add, and modify any file in this project. This personal project aims to challenge not just coding skills but also googling skills.

    ```plain
    LogInCLI/
    ├── README.md
    ├── __main__.py (Main Run File)
    └── src (Source Code)
        ├── app.py
        ├── backend.csv (Baskend Storage for Account Information)
        └── log (CLI Log for Tracking Activity)
    ```

* How to run the CLI

    The following command will run the whole project folder due to the `__main__.py` file inside the folder `./LogInCLI`.

    If you are inside the project folder.
    ```plain
    python3 ./ 
    ```

    If you are outside the project folder. 
    ```plain
    python3 ./LogInCLI
    ```

* Reference AnswerThe referenced answer will be released after one week.
