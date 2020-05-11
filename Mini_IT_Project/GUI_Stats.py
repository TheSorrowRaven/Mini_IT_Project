from tkinter import Frame
import GUI_Account
import Account
import Interfaces

class Statistics():

    def __init__(self, parent: Frame, guiAcc):

        self.guiAcc = guiAcc

        burger1 = guiAcc.accounts
        burger2 = guiAcc.categories
        burger3 = guiAcc.selectedAccount
        burger4 = guiAcc.selectedAccount.GetBalance()

        sum = 0
        for i in guiAcc.accounts:
            sum += i.GetBalance()

        print("Total balance of all Accounts: ", sum)

        transactions = []   #Contains BOTH ACCOUNTS Transactions
        # I will sort by time added
        for i in guiAcc.accounts:
            for j in i.transactions:
                transactions.append(j)


        #transactionsSortedTemp = [None] * len(transactions)
        for a in range(len(transactions)):
            for i in range(len(transactions) - 1):
                tempTransaction = transactions[i]
                tempTransaction2 = transactions[i+1]
                if (tempTransaction.creationDateTime < tempTransaction2.creationDateTime):
                    transactions[i] = tempTransaction
                    transactions[i+1] = tempTransaction2
                else:
                    transactions[i] = tempTransaction2
                    transactions[i+1] = tempTransaction

        for i in range(len(transactions)):
            print(i, " -> ", transactions[i].title, "Created in", transactions[i].creationDateTime)

        # Expected output: sorted all stuff that displays title and creation time from OLDEST to NEWEST

        #print(burger1, burger2, burger3, burger4)

        pass
    