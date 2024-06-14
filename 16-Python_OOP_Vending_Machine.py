# Complete the following class
'''
The VendingMachine class constructor should take one parameter: password
Inside the constructor, add three fields: balance, password, and items.
balance should be initialized to 0, and items should be initialized to an empty list

Add an add_item method for the admin, that takes in a name, price, and password:
-Assume the name is a str, and that price is always a positive int or float
-If the password is incorrect, print the message "Incorrect Password"
-Else, create a new item object with the name and price, and add it to the list of items

Add a purchase_item method for the user, that takes in an index, and pay:
-Assume the index is positive and within range, and that pay is always a positive int or float
-If the pay is not sufficient, return a tuple (None, pay)
-Else, make the transaction by adding the item price to balance and return a tuple (item, change)

The __str__ operator should return a string to display the vending machine detail in the following format:
Vending Machine Balance: (balance)
(item 1) : (price 1)
(item 2) : (price 2)

Hint: Use a for loop to iterate through the items and add the new line character '\n' to each line
'''

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name + ": " + str(self.price)
    
    def __repr__(self) -> str:
        return str(self)

class VendingMachine:
    def __init__(self, password):
        self.password = password
        self.balance = 0
        self.items = []
    
    def add_item(self, name, price, password):
        if password != self.password:
            print("Incorrect Password")
        else:
            self.items.append(Item(name, price))
    
    def purchase_item(self, index, pay):
        item = self.items[index]
        if pay < item.price:
            return (None, pay)
        else:
            self.balance += item.price
            change = pay-item.price
            return (item, change)

    def __str__(self):
        info = "Vending Machine Balance: " + str(self.balance) + "\n"
        for item in self.items:
            info += str(item) + "\n"
        return info

correct_password = "Summer"
wrong_password = "Wrong"

vm = VendingMachine(correct_password)
vm.add_item("Snickers", 1, correct_password)
vm.add_item("Twix", 0.8, correct_password)
vm.add_item("Oreos", 2, correct_password)
vm.add_item("Coca-Cola", 1.2, correct_password)
vm.add_item("Cheetos", 1.4, correct_password)
print(vm)

index = 0
pay = 1.5
print(vm.purchase_item(index, pay))
print(vm)




