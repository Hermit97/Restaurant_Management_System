import sys
class server:

    def __init__(self):
        self.tacos = 4.99

    
    def get_server_name(self):
        self.server_name = str(input("Enter your name"))
        if self.server_name.isdigit():
            print("No numbers allowed")
            sys.exit()
        
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
        if option == "yes":
            sys.exit()
        else:
            d.sign_out_message()

    def order(self):
        customer = input("what do you want to order? Enter 1 for a taco. Enter 2 for a burrito.")
        try:
            customer = int(customer)
        except:
            print("Only numbers")
            sys.exit()
        if customer == 1:
            print("You ordered a taco")
            self.tacos
        elif customer == 2:
            print("We dont got burritos")
        else:
            print("We dont have that!")

    def get_bill(self):
        print("Here is your bill")
        print("Bill: ", "$", self.tacos)
        

#Testing server function
d = server()
d.get_server_name()
d.sign_in()
d.sign_out()
d.order()
d.get_bill()
