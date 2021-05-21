import sys
import server

class ordering:

    def __init__(self):
        self.sourcream = .99
        self.onions = .50

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

    def condiments(self):
        customer = input("Enter which condiment you want. 1 for sourcream and 2 for onions")
        if customer == 1:
            print("You added sourcream")
        elif customer == 2:
            print("You added onions")
