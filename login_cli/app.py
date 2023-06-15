"""
Summary:
    Main App Structure of LogIn_CLI

Discription:
    LogIn_CLI has three main modules, `login module`, register module`, and 'exit'. 
    The `main_menu page` will control which module the user will go.
"""

from login_cli.frontend.frontend import Frontend 

class App:

    def run(self):

        while True:
            
            if Frontend.is_logged_in:

                page_choice = Frontend.main_menu_after_logged_page()

                if page_choice == 1:
                    Frontend.show_log_page()
                
                elif page_choice == 2:
                    Frontend.exit_app_page()    
            
            else:

                page_choice = Frontend.main_menu_page()

                if page_choice == 1:
                    Frontend.login_page()

                elif page_choice == 2:
                    Frontend.register_page()

                elif page_choice == 3:
                    Frontend.exit_app_page()

