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
        self.investmentDesc2.pack()
        self.proceedBtn.pack()

    def LoginMenu(self, parent: Frame):
            self.investmentDesc2.destroy()
            self.proceedBtn.destroy()
            if (self.login is None):
                self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.loginlabel.place(x = 400, y = 420, anchor = "center")
                self.login = Entry(master = parent, textvariable ="API Key", font = ("", 24))
                self.login.place(x = 800, y = 420, anchor = "center")
                self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.passwordlabel.place(x = 390, y = 460, anchor = "center")
                self.password = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
                self.password.place(x = 800, y = 460, anchor = "center")
                self.loginBtn = Button(master = parent, text="Login", command = lambda : self.MainScreen(parent))
                self.loginBtn.place(x = 1000, y = 520, anchor = "center")

            else:
                self.MainScreen(parent)
            

    def MainScreen(self, parent: Frame):
         
        #Post Login
        self.loginBtn.destroy()
        self.loginlabel.destroy()
        self.passwordlabel.destroy()
        self.data = Client(api_key_id= self.login.get() , api_key_secret= self.password.get())
        
        #Display current cryptobalance
        self.balancelabel = Label(master = parent, text="The current balance is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "nw", x = 61.0, y = 10)
        self.balancebtc = Label(master = parent, text = self.CryptoBalance(1) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancebtc.place(anchor = "nw", x = 61.0, y = 90)
        self.btcbal = Label(master = parent, text='BTC', font = ("", 26), bg = Constants.mainWindowBgColor)
        self.btcbal.place(anchor = 'nw', x = 300, y = 90)
        self.balanceeth = Label(master = parent, text = self.CryptoBalance(2) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balanceeth.place(anchor = "nw", x = 61.0 , y = 150)
        self.ethbal = Label(master = parent, text='ETH', font = ("", 26), bg = Constants.mainWindowBgColor)
        self.ethbal.place(anchor = 'nw', x = 300, y = 150)
        self.balancexrp = Label(master = parent, text = self.CryptoBalance(3) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancexrp.place(anchor = "nw",x = 61.0 , y = 210)
        self.xrpbal = Label(master = parent, text='XRP', font = ("", 26), bg = Constants.mainWindowBgColor)
        self.xrpbal.place(anchor = 'nw', x = 300, y = 210)

        #Display current prices
        self.balancelabel = Label(master = parent, text="The current price is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "nw", x = 61, y = 420)
        self.balancebtc = Label(master = parent, text = self.ShowPrice(1) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancebtc.place(anchor = "nw", x = 61 , y = 480)
        self.btclabel = Label(master = parent, text = 'BTC', font = ("",26), bg = Constants.mainWindowBgColor)
        self.btclabel.place(anchor = 'nw', x = 300, y = 480)
        self.balanceeth = Label(master = parent, text = self.ShowPrice(2) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balanceeth.place(anchor = "nw", x = 61 , y = 540)
        self.ethlabel = Label(master = parent, text = 'ETH', font = ("",26), bg = Constants.mainWindowBgColor)
        self.ethlabel.place(anchor = 'nw', x = 300, y = 540)
        self.balancexrp = Label(master = parent, text = self.ShowPrice(3) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancexrp.place(anchor = "nw", x = 61 , y = 600)
        self.xrplabel = Label(master = parent, text = 'XRP', font = ("",26), bg = Constants.mainWindowBgColor)
        self.xrplabel.place(anchor = 'nw', x = 300, y = 600)

        #Display Options Available to User
    
        
    def CryptoBalance(self, value):     #required to get data from Luno Site
        self.json_data = self.data.get_balances()
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
