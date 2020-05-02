# Raven
from tkinter import Frame
import Constants
import Interfaces
import Account

class GUI_Account(Interfaces.IOnSave):

    accounts = []

    def OnSave(self):
        self.Main.SaveData("AccountsList", self.accounts)

    def __init__(self, parent: Frame, main):
        self.Main = main
        super().__init__(main)
        self.accounts = main.GetSavedData("AccountsList")
    
        if (self.accounts is None):
            self.NewUserAccounts()
        else:
            self.LoadAccounts()

    def LoadAccounts(self):
        pass

    def NewUserAccounts(self):
        self.accounts = []
        cashAccount = Account.Account()
        self.accounts.append(cashAccount)