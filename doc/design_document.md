### Overview: main()
    Function main() execute the whole process. Under function main(), we have function reload() to reload usernames and passwords stored in file backend.csv. 
    Then the user has to input a command: 0 for register, 1 for login.

### Basic function: reload()
    Everytime we call function main(), we automatically call function reload().
    Function reload() will return a list of username and a list of password.

### Optional function: register()
    Function register() requires the user to input a new username.
    First check: username should not exist in previous username list.
    If pass, it requires the user to input its password.
    Second check: the length of password should be longer than 5.
    If pass, it requires the user to enter the same password.
    Third check: the two passwords should match with each other.
    If pass, the user registers successfully. Its registration info will be added to file backend.csv.

### Optional function: login()
    Function login() requires the user to input its username.
    First check: username exists.
    If pass, it requires the user to input its password.
    Second check: password matches username.
    If pass, the user logins successfully. Its login history will be added to file log.txt.
