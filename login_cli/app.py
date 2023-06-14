from login_cli.frontend.frontend import Frontend 

class App:

    def run(self):

        while True:

            page_choice = Frontend.main_menu_page()

            if page_choice == 1:
                Frontend.login_page()

            elif page_choice == 2:
                Frontend.register_page()

            elif page_choice == 3:
                Frontend.exit_app_page()

