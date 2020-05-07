# Fong

class BankAccount():

    def __init__(self, money): # When BankAccount is created, this will be instantly called
        self.amount = money # Upon creation, their money is set to 0

    def DepositMoney(self, money):
        self.amount = self.amount + money

    def WithdrawMoney(self, money):
        self.amount = self.amount - money

#over here is out of class, note indentation
