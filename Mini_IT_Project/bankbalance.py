# Fong

class BankAccount():

    def __init__(self): # When BankAccount is created, this will be instantly called
        self.amount = 0 # Upon creation, their money is set to 0

    def DepositMoney(self, money):
        self.amount = self.amount + money

    def WithdrawMoney(self, money):
        self.amount = self.amount - money

#over here is out of class, note indentation



myAcc = BankAccount()   # Object creation

myAcc.DepositMoney(20)      #So myAcc got 20 money

fongsAcc = BankAccount()  # Object creation

fongsAcc.DepositMoney(100)    #Fong's rich

fongsAcc.WithdrawMoney(10) #Taxes



print(myAcc.amount)
print(fongsAcc.amount)