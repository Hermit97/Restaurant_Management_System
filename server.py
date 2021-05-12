import sys
class server:

    def get_server_name(self):
        self.server_name = input("Enter your name")
        
    def greeting(self):
        print("welcome ",self.server_name) 
    
    def sign_out_message(self):
        print("Signing out " , self.server_name)

    def sign_in(self):

        option = input("Do you want to sign in? yes or no?")
        if option == "no":
            sys.exit()
        else:
            d.greeting()

    def sign_out(self):
        option = input("Do you want to sign out? yes or no?")

        if option == "no":
            sys.exit()
        else:
            d.sign_out_message()


#Testing server function
d = server()
d.get_server_name()
d.sign_in()
d.sign_out()






