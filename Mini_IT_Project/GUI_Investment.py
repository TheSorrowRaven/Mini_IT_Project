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
                self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.loginlabel.place(x = 400, y = 420, anchor = "center")
                self.login = Entry(master = parent, textvariable ="API Key", font = ("", 24))
                self.login.place(x = 800, y = 420, anchor = "center")
                self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.passwordlabel.place(x = 390, y = 460, anchor = "center")
                self.password = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
                self.password.place(x = 800, y = 460, anchor = "center")
                self.data = Client(api_key_id= self.login , api_key_secret= self.password)
                self.loginBtn = Button(master = parent, text="Login", command = lambda : self.MainScreen(parent))
                self.loginBtn.place(x = 1000, y = 520, anchor = "center")

            else:
                self.MainScreen(parent)
            

    def MainScreen(self, parent: Frame):
         
        #Post Login
        self.loginBtn.destroy()
        self.passwordlabel.destroy()

        #Display current cryptobalance
        self.balancelabel = Label(master = parent, text="The current balance is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "nw")
        self.balancebtc = Entry(master = parent, text = self.CryptoBalance(1) , bd =1)
        self.balancebtc.place(anchor = "nw", relx = 1.3 , rely = 1.5)
        self.balanceeth = Entry(master = parent, text = self.CryptoBalance(2) , bd =1)
        self.balanceeth.place(anchor = "nw", relx = 1.3 , rely = 1.5)
        self.balancexrp = Entry(master = parent, text = self.CryptoBalance(3) , bd =1)
        self.balancexrp.place(anchor = "nw", relx = 1.3 , rely = 1.5)

        #Display current prices
        self.balancelabel = Label(master = parent, text="The current price is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "ne")
        self.balancebtc = Entry(master = parent, text = self.CryptoBalance(1) , bd =1)
        self.balancebtc.place(anchor = "ne", relx = -1.3 , rely = -1.5)
        self.balanceeth = Entry(master = parent, text = self.CryptoBalance(2) , bd =1)
        self.balanceeth.place(anchor = "ne", relx = -1.3 , rely = -1.5)
        self.balancexrp = Entry(master = parent, text = self.CryptoBalance(3) , bd =1)
        self.balancexrp.place(anchor = "ne", relx = -1.3 , rely = -1.5)
        
    def CryptoBalance(self, value):     #required to get data from Luno Site
        self.json_data = self.data.get_tickers()
        if value == 1:
            self.bitcoinbal = self.json_data['balance'][2]['balance']
            return self.bitcoinbal

        elif value == 2:
            self.ethereumbal = self.json_data['balance'][0]['balance']
            return self.ethereumbal

        elif value == 3:
            self.xrpbal = self.json_data['balance'][3]['balance']
            return self.xrpbal

    def ShowPrice(self, value):
        self.json_data = self.data.get_tickers()
        if value == 1:
            self.bitcoinprice = self.json_data['tickers'][3]['ask']
            return self.bitcoinprice

        elif value == 2:
            self.ethereumprice = self.json_data['tickers'][1]['ask']
            return self.ethereumprice

        elif value == 3:
            self.xrpprice = self.json_data['tickers'][1]['ask']
            return self.ethereumprice

    #def BuyCoins(self, parent: Frame):      Planned future feature