# snake case - function names, variables def add_two
# camel case - class name, Student, CreditCard, and not credit_card

class CreditCard:
    def __init__(self, name, number, limit = 8000, bank = "Python Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0
        self.limit = limit
    
    def charge(self, amount):
        if not (isinstance(amount, int) or isinstance(amount, float)) or (amount <= 0):
            print ("Charge Denied")
        else:
            self.balance += amount
    
    def pay(self, amount):
        if not (isinstance(amount, int) or isinstance(amount, float)) or (amount <= 0):
            print ("Payment Denied")
        else:
            self.balance -= amount

    def __str__(self):
        info = "Name: " + self.name + "\n"
        info += "Number: " + "XXXX" + self.number[4:8] + "\n"
        info += "Bank: " + self.bank + "\n"
        info += "Balance:" + str(self.balance) + "\n"
        return info
    
    def __repr__(self):
        return str(self)


card = CreditCard("Kenny", "12345678")
print(card)

card.charge(10000)
print(card.balance)
card.pay(8000)
print(card.balance)





