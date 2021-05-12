class server:

    def get_server_name(self):
        self.server_name = input("Enter your name")
        
    def greeting(self):
        print("welcome ",self.server_name) 

    def sign_in(self):
        option = input("Do you want to sign in? yes or no?")

        if option == "no":
            sys.exit()
        else:
            self.get_server_name()


d = server()
d.get_server_name()
d.greeting()






