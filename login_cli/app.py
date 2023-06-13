from login_cli.frontend import frontend 

class App:

    def __init__(self):
        self.page_number = 0 

    def run(self):

        while True:

            print("pageNum", self.page_number)
            print("1 For Login, 2 For Register, 3 For Exit: ")
            self.page_number = int(input())

            if self.page_number == 1:
                frontend.login_module()
            elif self.page_number == 2:
                frontend.register_module()
            elif self.page_number == 9:
                frontend.success_login()
            elif self.page_number == 3:
                frontend.exit_app()

    def change_page(self, new_page_num):
        self.page_number = new_page_num