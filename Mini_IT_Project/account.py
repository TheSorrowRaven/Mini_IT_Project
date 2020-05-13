# Raven
import datetime

class Account():

    name = None

    def __init__(self):
        self.transactions = []

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


class BankAccount(Account): #Inheritance

    interestRate = 0    # In percentage, currently 0%

    def __init__(self):
        super().__init__() #Calls base class __init__()

    def SetInterests(self, interestRate):
        self.interestRate = interestRate

    def GainInterests(self):

        if self.interestRate == 0:
            return

        currentBalance = super().GetBalance()
        # SO basically from here is basic maths
        gainedInterest = currentBalance * self.interestRate / 100

        transaction = Transaction()
        transaction.amount = gainedInterest
        transaction.isIncome = True
        transaction.category = None # We set as None otherwise will be super super complicated
        transaction.title = "Interests"
        transaction.description = str(datetime.datetime.now()) + " Added" # Over here we can be creative, by setting when the interest is gained
        transaction.date = datetime.date.today()
        transaction.creationDateTime = datetime.datetime.now()
        transaction.otherSubject = "Bank"   # Over here I dk what it's called but I'll say BANK paid the interests

        #So all done

        super().AddTransaction(transaction) # Over here we just add into the list


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


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
