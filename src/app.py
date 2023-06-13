class App:

    page_number = 0 

    def run(self):

        while True:
            
            print("1 For Login, 2 For Register, 3 For Exit: \n")
            self.page_number = int(input())

            if self.page_number == 1:
                print("LOGIN")
            elif self.page_number == 2:
                print("REGISTER")
            elif self.page_number == 3:
                break 
            
            

    def change_page(self, new_page_num):
        self.page_number = new_page_num
    
    
    
