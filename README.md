# 🔐LogInCLI

## 📄Summary

Design and develop a simple login CLI (Command Line Interface) application. The CLI provides `User Register` and `User Login`. Besides the two main services, the CLI also outputs a log file to track the login record.

1. Make a branch from the latest `main` branch.

2. Develop the CLI locally.

3. Publish your branch to the repo.

4. Create a release.

🚫DON'T PULL REQUEST or MERGE YOUR BRANCH INTO THE MAIN BRANCH!

---

## 👀MUST READ BEFORE DEVELOPING

Here are a few important concepts involved with the project. My suggestion is to read through all the articles first to have a brief understanding from a higher-level viewpoint. You don't need to 100% follow the reference because a few of them are too deep, and it is not suitable for this tiny project.

Read through all the articles roughly once, and then pick the important concepts you need to implement on the project!

* ### Package & Module❗

    **<https://docs.python.org/3/tutorial/modules.html>**

    **<https://www.programiz.com/python-programming/package>**

    **<https://www.geeksforgeeks.org/python-packages/>**

* ### Python Project Structure Layout❗

    **<https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6>**

    **<https://medium.com/mlearning-ai/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95>**

    **<https://docs.python-guide.org/writing/structure/>**

* ### Markdown File Cheatsheet

    **<https://www.markdownguide.org/cheat-sheet/>**

---

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

* Design Doc Markdown

    Tell people how you design the CLI and how a user can use the CLI.

---

## 🏨Project Structure Template Recommendations

* The template structure

    I draft the struct based on my personal preference, it's all good for you to use your template. You will freely delete, edit, add, and modify any file in this project. This personal project aims to challenge not just coding skills but also googling skills.

    ```plain
    LogInCLI/
    ├── README.md
    ├── __main__.py (application run point)
    ├── doc
    │   └── design_document.md (the design document and user manual)
    └── src
        ├── app.py (the code)
        ├── backend.csv (backend database to store the user information)
        └── log.txt (track the login activity)
    ```

* How to run the CLI

    The following command will run the whole project folder due to the `__main__.py` file inside the folder `./LogInCLI`.

    If you are inside the project folder ( `LogInCLI/` )

    ```plain
    python3 ./ 
    ```

    If you are outside the project folder.

    ```plain
    python3 ./LogInCLI
    ```

* Reference Answer

    The referenced project design will be released after one week.
