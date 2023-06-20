# Register an account, login, and exit the program.

The `register()` function handles the registration process.
It prompts the user to enter a username and checks if it is valid (not empty) and unique by comparing it to existing usernames in the backend.csv. If the username is invalid or already exists, error messages are displayed. The function then prompts the user to enter a password and ensures that it is valid (not empty). Finally, it writes the username and password to the backend.csv and displays a success message.

The `login()` function handles the login process.
It prompts the user to enter their username and password. It reads the backend.csv and compares the entered username and password with the stored values. If a match is found, a success message is displayed, and the login time along with the username is written to the log file. If the entered credentials do not match any stored values, an error message is displayed.

The `main()` function acts as the entry point of the program.
It presents the user with options to register, login, or exit by input. Depending on the chosen option, it calls the corresponding function (`register()`, `login()`, or `exit()`). If an invalid choice is made, an error message is displayed.
