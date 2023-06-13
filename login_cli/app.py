from login_cli.frontend.frontend import Frontend 

class App:

    def run(self):

        while True:

            Frontend.main_menu_page()

            if Frontend.page_tag == 1:
                Frontend.login_page()

            elif Frontend.page_tag == 2:
                Frontend.register_page()

            elif Frontend.page_tag == 3:
                Frontend.exit_app_page()

