from tkinter import Frame
import GUI_Account
import Account
import Interfaces

class Statistics():

    def __init__(self, parent: Frame):
        print("Console test - Statistics Init with frame: ", parent)
        self.checker = GUI_Account.GUI_Account(self, parent)
        burger1 = self.checker.accounts
        burger2 = self.checker.categories
        burger3 = self.checker.selectedAccount
        burger4 = Account.Account.GetBalance(self)

        print(burger1, burger2, burger3, burger4)

        pass
    