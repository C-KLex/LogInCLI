# What is in Jordan CLI

## 1. First it gives user a warm welcome language and let the user choose which action to go with.

&nbsp;

## 2. If the user choose to login, we have a login function for it (Part 3); if the user chooses to register, we have a register function handling that (Part 4).

&nbsp;

## 3. When the user is logging in, the login function will check if the username and password are both right.

### 3.1 If they are both right, it's a successful login, so it will send the user feedback as **_Successful Logged in! Welcome Back!_**, and then record this log-in history in _log_ with the log-in time and username.

### 3.2 If the username is right while the password is wrong, it will send the user feedback as **_Wrong password, please try again._**

### 3.3 If neither the username nor the password were right, it give the feedback as **_Log-in not successful, please try again. (If not registered please register first.)_**

&nbsp;

## 4. When the user is registering, the register function will require the username and password from them.

### 4.1 The function will fist check if the username is already there. If it is, it will return **_Account already exists, please log-in or change an user name and try again._**

### 4.2 If not, it will first put the username and password in backend.csv, and then return **_Registered Successfully!_**
