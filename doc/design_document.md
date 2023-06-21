# Register an account, login, and exit the program.

## login_register.py

- The `no_empty()` function is used to validate input and ensure it is not empty. The function returns the non-empty value.

- The `register()` function handles the registration process. It uses the no_empty function to get a non-empty username from the user. Then, it checks if the entered username already exists in the backend.csv file. If exists, it prompts the user to choose a different username. If the username is unique, the function proceeds to ask for a non-empty password using the no_empty function. Finally, it writes the username and password to the backend.csv and displays a success message.

- The `login()` function handles the login process.
  It prompts the user to enter their username and password. It reads the backend.csv and compares the entered username and password with the stored values. If the entered username doesn't exist, a "Username not found" message is displayed, prompting the user to register first. If the username exists, it verifies if the entered password matches the stored password for that username. If a match is found, a success message is displayed, and the login time along with the username is written to the log file. Otherwise, an "Invalid password" message is displayed.

#

## app.py

- The `main()` function acts as the entry point of the program. It presents the user with options to register, login, or exit by input. Depending on the chosen option, it calls the corresponding function (`register()`, `login()`, or `exit()`). If an invalid choice is made, an error message is displayed.
