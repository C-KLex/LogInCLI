"""
SUMMARY:
    The frontend of LogIn_CLI
"""

from login_cli.backend.backend import Backend

class Frontend:

    is_logged_in = False

    ##### LOGIN MODULE #####
    @classmethod
    def login_page(cls):

        cls._module_title("##### LOGIN MODULE #####")

        for log_in_try_number in range(1, 4):
            
            username = input("USERNAME: ")
            password = input("PASSWORD: ") 

            if not Backend.account_exist(username):
                cls.account_not_exist_page() 
                return 
            
            if not_valid := not Backend.login_validation(username, password):
                print("!! WRONG CREDENTIAL, YOU CAN TRY ", 3 - log_in_try_number, " TIMES !!\n")

            else:
                cls.is_logged_in = True
                cls.login_success_page(username)
                return 

        cls.login_fail_page()
        return  

    @classmethod
    def account_not_exist_page():
        print("!! ACCOUNT NOT EXIST !!")
        print("!! PLEASE REGISTER FIRST !!")
        return 

    @classmethod
    def login_fail3_page(cls):
        print("!!!!! LOGIN FAIL !!!!!")
        quit()

    @classmethod
    def login_success_page(cls, username):
        print("!!!!! LOGIN SUCCESS, HI! ", username, " !!!!!")
        quit()

    ##### REGISTER MODULE #####   
    @classmethod
    def register_page(cls):
        
        cls._module_title("##### REGISTER MODULE#####")
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        
        if Backend.account_exist(username):
            cls.account_exist_page()
            return 

        Backend.add_account(username, password)

        cls.register_success_page()
        
        return 

    @classmethod
    def register_success_page(cls):
        print("!! REGISTER SUCCESS !!\n")
        return 

    @classmethod
    def account_exist_page(cls):
        print("!! ACCOUNT ALREADY EXISTS !!\n")
        return 

    ##### EXIT APP PAGE #####
    @classmethod
    def exit_app_page(cls):
        if cls.is_logged_in:
            print("!! LOGOUT SUCCESSFUL !!\n")
        else:
            print("!! CLOSING APP !!")
        quit()

    @classmethod
    def logout_page(cls):
        print("!! LOGOUT SUCCESSFULLY !!")
        cls.is_logged_in = False
        return 

    ##### MAIN PAGE #####     
    @classmethod
    def main_menu_page(cls):
        cls._module_title("##### MAIN MENU #####")
        return int(input("!! 1 For Login, 2 For Register, 3 For Exit: !!\n"))
    
    @classmethod
    def _module_title(cls, title):
        print(title, "\n")
        return