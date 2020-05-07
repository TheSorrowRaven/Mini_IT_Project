# Raven

import datetime

class Account():

    name = None
    balance = 0
    transactions = []

    def __init__(self):



        pass

    def EarnAmount(self, amount):
        self.balance += amount
    
    def LoseAmount(self, amount):
        self.balance -= amount

    def CreateTransaction(self, amount, category, title, description, dateTime, otherSubject):
        transaction = Transaction()
        transaction.amount = amount
        transaction.category = category
        transaction.title = title
        transaction.description = description
        transaction.dateTime = dateTime
        transaction.otherSubject = otherSubject

    def AddTransaction(self, transaction):
        self.transactions.append(transaction)

    def Interest(self):


class Transaction():
    amount = 0
    category = None
    title = None
    description = None
    dateTime = None
    creationDateTime = None
    otherSubject = None

    def __init__(self):
        self.creationDateTime = datetime.datetime.now()

    def printData(self):
        print("Amount: {}, Title: {}, Desc: {}, Other Subject: {}".format(self.amount, self.title, self.description, self.otherSubject))

class Category():
    parent = None
    name = ""
    
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent

    pass

class BankAccount():

    def __init__(self): # When BankAccount is created, this will be instantly called
        self.amount = 0 # Upon creation, their money is set to 0

    def DepositMoney(self, money):
        self.amount = self.amount + money

    def WithdrawMoney(self, money):
        self.amount = self.amount - money
