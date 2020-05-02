# Raven

class Account():

    balance = 0

    def __init__(self):



        pass

    def EarnAmount(self, amount):
        self.balance += amount
    
    def LoseAmount(self, amount):
        self.balance -= amount

class Transaction():
    cash = 0
    category = None

class Category():
    pass