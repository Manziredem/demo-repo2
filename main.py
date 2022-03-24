### creating an instance is simolar to creating an object
###  NB: methodes = functions inside the clasess
### by default, python pass 'self' argument bydefaulf

from unicodedata import name


class Item:
    def __init__(self, name):
        return(f"instance created: {name}")
    def calculate_total_price(self, x, y):
        return x * y

# create an instance of a class
item1 = Item("phone")
## assigne attributed to the instances of class/instances
item1.name = "phone"
item1.price = 100
item1.quantity = 5
#print(item1.calculate_total_price(item1.price, item1.quantity))

#other instance

item2 = Item("laptop")
item2.name = "laptop"
item2.price = 1000
item2.quantity = 3
#print(item2.calculate_total_price(item2.price, item2.quantity))
