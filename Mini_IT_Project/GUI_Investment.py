# Naga
from tkinter import Frame, ttk, Entry, Label, Button, Canvas, Toplevel
from luno_python.client import Client
import Constants
import tkinter.messagebox

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

            def LoginTest(login, password):
                self.api = login.get()      #Save before deleting the widget            
                self.secret = password.get()
                print(self.api)
                print(self.secret)
                self.data = Client(api_key_id= self.api , api_key_secret= self.secret)
                
                #Test login before letting user log in     
                try:
                    trial = self.data.get_balances()
                    print(trial)
                    self.MainScreen(parent)

                except Exception as e:
                    print(e)
                    tkinter.messagebox.showerror(title="Login Error", message="Invalid api key or api key secret, please try again")

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
                self.loginBtn = Button(master = parent, text="Login", command = lambda : LoginTest(self.login, self.password))
                self.loginBtn.place(x = 1000, y = 520, anchor = "center")

            else:
                self.api = self.login.get()      #Save before deleting the widget            
                self.secret = self.password.get()
                self.data = Client(api_key_id= self.api , api_key_secret= self.secret)
                self.MainScreen(parent)


    def MainScreen(self, parent: Frame):
         
        #Post Login
        self.loginBtn.destroy()
        self.loginlabel.destroy()
        self.passwordlabel.destroy()
        self.login.delete(0)
        self.password.delete(0)

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
        self.balancebtc.place(anchor = "nw", x = 300 , y = 480)
        self.btclabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.btclabel.place(anchor = 'nw', x = 61, y = 480)
        self.balanceeth = Label(master = parent, text = self.ShowPrice(2) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balanceeth.place(anchor = "nw", x = 300 , y = 540)
        self.ethlabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.ethlabel.place(anchor = 'nw', x = 61, y = 540)
        self.balancexrp = Label(master = parent, text = self.ShowPrice(3) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancexrp.place(anchor = "nw", x = 300 , y = 600)
        self.xrplabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.xrplabel.place(anchor = 'nw', x = 61, y = 600)
        self.configbtn = Button(text="Manage crypto", command = self.CoinOption)
        self.configbtn.place(x = 700, y = 120, anchor = "nw")

            
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
            self.xrpprice = self.json_data['tickers'][14]['ask']
            return self.xrpprice
    

    def CoinOption(self):       #Buy or Sell a Coin
        self.configbtn.destroy()
        self.optionwindow = Toplevel()               #opens a new window for user to decide
        self.labelinfo = Label(self.optionwindow, text='Would you like to :', font = ("", 26), bg = Constants.mainWindowBgColor)
        self.buy = Button(self.optionwindow, text="Buy coins", command = self.BuyCoins)
        self.buy.place(anchor ='nw')
        self.sell = Button(self.optionwindow, text="Sell Coins", command = self.SellCoins)
        self.sell.place(anchor ='ne')
        self.buy.pack()
        self.sell.pack()

    def CryptoinRM(self, buysell, function):      #Display coin value in RM
        try:
            actualbuy = float(buysell)
            thevalue = float(self.ShowPrice(1))
            if function == 1:
                self.currencycalc = actualbuy * thevalue
            elif function == 2:
                self.currencycalc = actualbuy / thevalue
            else:
                print('The Master Chief is an anime weeb')

            print(self.currencycalc)
            self.textdisplay = "RM {}" 
            self.actualtextdisplay = self.textdisplay.format(self.currencycalc)
            self.currencydisplay = Label(self.optionwindow, text = self.actualtextdisplay, font = ("", 26), bg = Constants.mainWindowBgColor)
            self.currencydisplay.grid(row=1, column=1)
        
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror(title="Input Error", message="Invalid input")

    def BuyCoins(self):

        self.buy.destroy()
        self.sell.destroy()

        def ConfirmMsgBox(value, crypto):

            tkinter.messagebox.showinfo("Confirm Transaction", "Would you like to proceed with transaction of {} {}?".format(value, crypto))

        def FunctionDestroyer():      #Destroys widget without repetitive code
            self.buybtcbtn.destroy()
            self.buyethbtn.destroy()
            self.buyxrpbtn.destroy()
           
        def BTC():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter BTC to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.btcbuy = Entry(self.optionwindow, textvariable ="Total BTC", font = ("", 24))
            self.btcbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.btcbuy.get(), 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : ConfirmMsgBox(self.btcbuy.get(), "BTC"))
            self.confirmbuy.grid(row=2, column=1)

        def ETH():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter ETH to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.ethbuy = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethbuy.get(), 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = ConfirmMsgBox(self.ethbuy, "ETH"))
            self.confirmbuy.grid(row=2, column=1)

        def XRP():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter XRP to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.xrpbuy = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpbuy.get(), 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = ConfirmMsgBox(self.xrpbuy, "XRP"))
            self.confirmbuy.grid(row=2, column=1)
        
        self.buybtcbtn = Button(self.optionwindow, text="Buy BTC", command = BTC)
        self.buybtcbtn.grid(anchor = 'nw')
        self.buyethbtn = Button(self.optionwindow, text="Buy ETH", command = ETH)
        self.buyethbtn.grid(anchor = 'center')
        self.buyxrpbtn = Button(self.optionwindow, text="Buy XRP", command = XRP)
        self.buyxrpbtn.grid(anchor = 'ne')
        self.buybtcbtn.pack()
        self.buyethbtn.pack()
        self.buyxrpbtn.pack()

    def SellCoins(self):

        self.buy.destroy()
        self.sell.destroy()

        def ConfirmMsgBox(value, crypto):
            tkinter.messagebox.showinfo("Confirm Transaction", "Would you like to proceed with transaction of {} {}?").format(value, crypto)

        def FunctionDestroyer():      #Destroys widget without repetitive code
            self.sellbtcbtn.destroy()
            self.sellethbtn.destroy()
            self.sellxrpbtn.destroy()

        def BTC():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter BTC to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.btcsell = Entry(self.optionwindow, textvariable ="Total BTC", font = ("", 24))
            self.btcsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.btcsell.get(), 2))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = ConfirmMsgBox(self.btcsell, "BTC"))
            self.confirmsell.grid(row=2)

        def ETH():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter ETH to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.ethsell = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethsell.get(), 1))
            self.viewbuy.grid(row=1, column=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = ConfirmMsgBox(self.ethsell, "ETH"))
            self.confirmsell.grid(row=2, column=1)

        def XRP():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter XRP to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.xrpsell = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpsell.get(), 1))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = ConfirmMsgBox(self.xrpsell, "XRP"))
            self.confirmsell.grid(row=2, column=1)

        self.sellbtcbtn = Button(self.optionwindow, text="Sell BTC", command = BTC)
        self.sellbtcbtn.place(anchor = 'nw')
        self.sellethbtn = Button(self.optionwindow, text="Sell ETH", command = ETH)
        self.sellethbtn.place(anchor = 'center')
        self.sellxrpbtn = Button(self.optionwindow, text="Sell XRP", command = XRP)
        self.sellxrpbtn.place(anchor = 'ne')
        self.sellbtcbtn.pack()
        self.sellethbtn.pack()
        self.sellxrpbtn.pack()

