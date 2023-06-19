# 🔒LogIn_CLI Design Doc

## 🏦CLI Structure

* Layout of the APP, Without Irrelevant File

    The layout only show the working python script. There is not doc file, database file, and log file, etc.

    ```plain
    LogInCLI/
        ├── __main__.py (application run point)
        ├── setup.py (application set up)
        └── login_cli (APP Package)
            ├── app.py (main file of login_cli)
            ├── backend/ (backend package)
            ├── tests/ (pytest code)
            └── frontend/ (frontend package)
    ```

* Main APP Layout (`app.py`)

    There are two scenarios, logged-in or not logged-in. Each scenario provides several modules for user to interact with. For example, before logging in, the APP will provide three options to choose, `log in`, `register`, `exit`. After logging in, the APP will provide two options, `show logs` and `exit`.  

    ```python
    class App:
        def run(self):
            while True:
                
                if Frontend.is_logged_in:

                    page_choice = Frontend.main_menu_after_logged_page()

                    if page_choice == 1:
                        Frontend.show_log_page()

                    elif page_choice == 2:
                        Frontend.exit_app_page()    
                
                else:

                    page_choice = Frontend.main_menu_page()

                    if page_choice == 1:
                        Frontend.login_page()

                    elif page_choice == 2:
                        Frontend.register_page()
                        
                    elif page_choice == 3:
                        Frontend.exit_app_page()
    ```

* Backend Database

    After running the `setup.py`, `backend.csv` and `log.txt` will be generated in the package. `backend.csv` aims to store the user registration information and the other aims to record the user log in history.

    ```plain
    login_cli/
    ├── __init__.py
    ├── app.py
    ├── backend
    │   ├── backend.csv
    │   ├── backend.py
    │   └── log.txt
    ├── frontend
       └── frontend.py
    ```

## 📚User Manual

1. Run the `setup.py`

    It will create the backend database.

    ⛔Warning: The backend database will be erased if the database has been created already.

        $ python3 setup.py

2. Run the CLI

        $ python3 ./

## 🤚Warning

* Input Validation

    If the User type non-integer, space, or empty string, the APP will give error and stop working.

* Space Key Avoidance

    The APP also take the space key as part of the string. For example, "foo" and "foo " are different for the APP, for human, however, they look the same on the command line. This will cause unnessary mistake while typing the log in information.

* Database Missing Error

    If one of the database is missing (backend.csv or log.txt), the APP won't notify WHICH one is missing but notify "DATABASE HAS ERROR". User can't tell which database has error, so the user can only reset all the database, and the action may erase all the existing data entries.
