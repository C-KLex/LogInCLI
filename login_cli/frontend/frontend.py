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

            if valid := Backend.login_validation(username, password):
                cls.login_success_page(username)

            else:
                print("WRONG CREDENTIAL, YOU CAN TRY ", 3 - log_in_try_number, " TIMES \n")

        cls.login_fail_page()

    @classmethod
    def login_fail_page(cls):
        print("##### LOGIN FAIL #####")
        quit()

    @classmethod
    def login_success_page(cls, username):
        print("##### LOGIN SUCCESS, HI! ", username, " #####")
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

    @classmethod
    def register_success_page(cls):
        print("!! REGISTER SUCCESS !!\n")

    @classmethod
    def account_exist_page(cls):
        print("!!ACCOUNT ALREADY EXISTS !!\n")


    ##### EXIT APP PAGE #####
    @classmethod
    def exit_app_page(cls):
        if cls.is_logged_in:
            print("!! LOGOUT SUCCESSFUL !!\n")
        else:
            print("!!CLOSING APP!!")
        quit()


    ##### MAIN PAGE #####     
    @classmethod
    def main_menu_page(cls):
        cls._module_title("##### MAIN MENU #####")
        return int(input("1 For Login, 2 For Register, 3 For Exit: \n"))




    @classmethod
    def _module_title(cls, title):
        print(title, "\n")