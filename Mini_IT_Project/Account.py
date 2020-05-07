# Raven

import datetime

class Account():

    name = None

    def __init__(self):
        self.transactions = []


        pass

    def GetBalance(self):
        calcBalance = 0
        for i in self.transactions:
            if (i.isIncome):
                calcBalance += i.amount
            else:
                calcBalance -= i.amount
        return calcBalance

    def AddTransaction(self, transaction):
        self.transactions.append(transaction)


class Transaction():
    amount = 0
    isIncome = True
    category = None
    title = None
    description = None
    date = None
    creationDateTime = None
    otherSubject = None

    def __init__(self):
        self.creationDateTime = datetime.datetime.now()

class Category():
    parent = None
    name = ""
    
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent

    def GetFullPath(self) -> str:
        loop = True
        i = self
        text = self.name
        while loop:
            i = i.parent
            if i is None:
                loop = False
            else:
                text = i.name + " - " + text
        return text

    pass

class BankAccount():
    def __init__(self): # When BankAccount is created, this will be instantly called
        self.amount = 0 # Upon creation, their money is set to 0

    def DepositMoney(self, money):
        self.amount = self.amount + money

    def WithdrawMoney(self, money):
        self.amount = self.amount - money
