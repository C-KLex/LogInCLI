class Backend:

    @classmethod
    def login_validation(cls, username, password):
        return False 
    
    @classmethod
    def account_exist(cls, username):
        return False
    
    @classmethod
    def add_account(cls, username, password):
        print("add account")