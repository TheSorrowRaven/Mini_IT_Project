# Naga
from tkinter import Frame, ttk, Entry, Label, Button, Canvas, PhotoImage
from luno_python.client import Client
import Constants

class GUI_Investment:

    def OnSave(self):
        self.Main.SaveData("API Key", self.login)
        self.Main.SaveData("API Secret", self.password)

    def __init__(self, parent: Frame, main): 
        self.Main = main
        self.parent = parent  
        super().__init__()
        self.login = main.GetSavedData("API Key")
        self.password = main.GetSavedData("API Secret")
        self.investmentDesc2 = Label(master = parent, text = "Please signup first from the Luno Website", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc2.place(x = 600, y = 360, anchor = "center")
        self.proceedBtn = Button(master = parent, text="Proceed" , command = lambda : self.LoginMenu(parent)) #might change bg in a later date
        self.proceedBtn.place(x = 660, y = 420, anchor = "center")

    def LoginMenu(self, parent: Frame):
            self.investmentDesc2.destroy()
            if (self.login is None):
                self.selectedAccount = self.login[0]
                self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.loginlabel.place(x = 400, y = 420, anchor = "center")
                self.login = Entry(master = parent, textvariable ="API Key", font = ("", 24))
                self.login.place(x = 800, y = 420, anchor = "center")
                self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.passwordlabel.place(x = 390, y = 460, anchor = "center")
                self.password = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
                self.password.place(x = 800, y = 460, anchor = "center")
            
            self.loginBtn = Button(master = parent, text="Login", command = self.MainScreen)
            self.loginBtn.place(x = 1000, y = 520, anchor = "center")
            data = Client(api_key_id= self.login , api_key_secret= self.password)     #required to get data from Luno Site

    def MainScreen(self):
        self.loginBtn.destroy()    #Test improper function in OOP

        pass

    def ShowPrices(self, parent: Frame):

        pass

    def CurrentBalance(self, parent: Frame):

        pass

    #def BuyCoins(self, parent: Frame):      Planned future feature