import ordering
import server

class bill:

    def __init__(self):
        self.bill = 0.00
    
    def get_bill(self):
        if ordering.order() == 1:
            self.bill = .99
        elif ordering.order() == 2:
            self.bill = .50



    def ask_bill(self):
        customer = input("Are you ready for the bill")
        if customer == 1:
            print("yes I am ready for the bill")
            print("Your bill is " + get_bill())
        elif customer == 2:
            sys.exit()



