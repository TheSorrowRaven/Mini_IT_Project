#/***************************************************
#File Name: gui_investment.py
#Version/Date: 0.9 (2020-05-13)
#Programmer/ID: Nagaindran A/L Kanaseelanayagam (1191100776)
#Project Name: Smart Finance Manager 
#Teammates: Raven Lim Zhe Xuan, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###
from tkinter import Button, Canvas, Entry, Frame, Label, StringVar,OptionMenu, Toplevel, ttk
from luno_python.client import Client
import constants as Constants
import tkinter.messagebox

class GUI_Investment:

    api_key = []
    api_secret = []

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
        self.investmentDesc2.place(x = 660, y = 360, anchor = "center")
        self.proceedBtn = Button(master = parent, text="Proceed" , command = lambda : self.LoginMenu(parent)) #might change bg in a later date
        self.proceedBtn.place(x = 660, y = 420, anchor = "center")

    def LoginMenu(self, parent: Frame):

            def NewLogin():
                self.login = []
                self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.loginlabel.place(x = 400, y = 420, anchor = "center")
                self.logino = Entry(master = parent, textvariable ="API Key", font = ("", 24))
                self.logino.place(x = 800, y = 420, anchor = "center")
                
                self.login.append(self.logino)

            def NewPassword():
                self.password = []
                self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.passwordlabel.place(x = 390, y = 460, anchor = "center")
                self.passwordo = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
                self.passwordo.place(x = 800, y = 460, anchor = "center")

                self.password.append(self.passwordo)

            def LoginTest(logintest, passwordtest):
                logintest = logintest.get()
                passwordtest = passwordtest.get()
                self.data = Client(api_key_id= logintest , api_key_secret= passwordtest)

                print(passwordtest)
                
                #Test login before letting user log in     
                try:
                    trial = self.data.get_balances()
                    print(trial)
                    self.MainScreen(parent)

                except Exception as e:
                    self.login = []
                    self.password = []
                    print(e)
                    tkinter.messagebox.showerror(title="Login Error", message="Invalid api key or api key secret, please try again")

            self.investmentDesc2.destroy()
            self.proceedBtn.destroy()
            if (self.login is None):
                NewLogin()
                NewPassword()
                self.logininput = self.login[0]
                self.passwordinput = self.password[0]
                self.loginBtn = Button(master = parent, text="Login", command = lambda : LoginTest(self.logininput, self.passwordinput))
                self.loginBtn.place(x = 1000, y = 520, anchor = "center")

            else:
                self.logindata = self.login[0]
                self.passworddata = self.password[0]
                self.logindata = self.logindata.get()
                self.passworddata = self.passworddata.get()
                self.data = Client(api_key_id= self.logindata , api_key_secret= self.passworddata)
                self.MainScreen(parent)

    def DropDownMenus(self, parent: Frame):
        WalletList = ['option1', 'option2', 'option3', 'option4']
        variabledefault = StringVar(parent)
        variabledefault.set(WalletList[0])

        options = OptionMenu(parent, variabledefault, *WalletList)
        options.config(width = 25, font=("", 15))
        options.place(anchor = 'nw', x = 61.0 , y = 50)

    def MainScreen(self, parent: Frame):
         
        #Post Login
        self.loginBtn.destroy()
        self.loginlabel.destroy()
        self.passwordlabel.destroy()
        self.logino.destroy()
        self.passwordo.destroy()

        #Display current cryptobalance
        self.DropDownMenus(parent)
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
        self.balancebtc.place(anchor = "nw", x = 200 , y = 480)
        self.btclabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.btclabel.place(anchor = 'nw', x = 61, y = 480)
        self.balanceeth = Label(master = parent, text = self.ShowPrice(2) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balanceeth.place(anchor = "nw", x = 200 , y = 540)
        self.ethlabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.ethlabel.place(anchor = 'nw', x = 61, y = 540)
        self.balancexrp = Label(master = parent, text = self.ShowPrice(3) ,font = ("", 20), bd =1, bg = 'seashell3')
        self.balancexrp.place(anchor = "nw", x = 200 , y = 600)
        self.xrplabel = Label(master = parent, text = 'RM', font = ("",26), bg = Constants.mainWindowBgColor)
        self.xrplabel.place(anchor = 'nw', x = 61, y = 600)
        self.configbtn = Button(master = parent, text="Manage crypto", command = self.CoinOption)
        self.configbtn.place(x = 700, y = 120, anchor = "nw")
        self.configtransc1 = Button(master = parent, text="See BTC Transactions", command = lambda: self.TransactionHistory(1))
        self.configtransc1.place(x = 700, y = 160, anchor = "nw")
        self.configtransc2 = Button(master = parent, text="See ETH transactions", command = lambda: self.TransactionHistory(2))
        self.configtransc2.place(x = 700, y = 200, anchor = "nw")
        self.configtransc3 = Button(master = parent, text="See XRP Transactions", command = lambda: self.TransactionHistory(3))
        self.configtransc3.place(x = 700, y = 240, anchor = "nw")

    def CreateAccount(self, value):
        pass

    def TransactionHistory(self, value):       #Get transaction history
        self.json_data = self.data.get_balances()
        self.json_data = self.json_data['balance']

        if value == 1:
            for i in self.json_data:
                if i['asset'] == 'XBT':
                    self.id = i['account_id']
                    print(self.id)

        if value == 2:
            for i in self.json_data:
                if i['asset'] == 'ETH':
                    self.id = i['account_id']

        elif value == 3:
            for i in self.json_data:
                if i['asset'] == 'XRP':
                    self.xrpid = i['account_id']

        min_row = 0
        max_row = 1000
        transactionlist = self.data.list_transactions(self.id, max_row, min_row)
        print(transactionlist)
        
    def CryptoBalance(self, value):     #required to get data from Luno Site
        self.json_data = self.data.get_balances()
        self.json_data = self.json_data['balance']

        if value == 1:
            for i in self.json_data:
                if i['asset'] == 'XBT':
                    self.bitcoinbal = i['balance']
                    return self.bitcoinbal

        if value == 2:
            for i in self.json_data:
                if i['asset'] == 'ETH':
                    self.ethereumbal = i['balance']
                    return self.ethereumbal

        elif value == 3:
            for i in self.json_data:
                if i['asset'] == 'XRP':
                    self.xrpbal = i['balance']
                    return self.xrpbal

    def ShowPrice(self, value):
        self.json_data = self.data.get_tickers()
        self.json_data = self.json_data['tickers']

        if value == 1:
            for i in self.json_data:
                if i['pair'] == 'XBTMYR':
                    self.bitcoinprice = i['ask']
                    float(self.bitcoinprice)
                    return self.bitcoinprice

        elif value == 2:
               for i in self.json_data:
                if i['pair'] == 'ETHMYR':
                    self.ethereumprice = i['ask']
                    float(self.ethereumprice)
                    return self.ethereumprice

        elif value == 3:
            for i in self.json_data:
                if i['pair'] == 'XRPMYR':
                    self.xrpprice = i['ask']
                    float(self.xrpprice)
                    return self.xrpprice


    def CoinOption(self):       #Buy or Sell a Coin
        self.optionwindow = Toplevel()               #opens a new window for user to decide
        self.labelinfo = Label(self.optionwindow, text='Would you like to :', font = ("", 26), bg = Constants.mainWindowBgColor)
        self.buy = Button(self.optionwindow, text="Buy coins", command = self.BuyCoins)
        self.buy.place(anchor ='nw')
        self.sell = Button(self.optionwindow, text="Sell Coins", command = self.SellCoins)
        self.sell.place(anchor ='ne')
        self.buy.pack()
        self.sell.pack()

    def CryptoinRM(self, buysell, crypto, function):      #Display coin value in RM
 
        try:
            actualbuy = float(buysell)
            if crypto == 'BTC':
                thevalue = self.ShowPrice(1)

            elif crypto == 'ETH':
                thevalue = self.ShowPrice(2)

            elif crypto == 'XRP':
                thevalue = self.ShowPrice(3)

            else:
                print('Halo Infinite this July! :3')

            if function == 1:
                self.currencycalc = actualbuy * thevalue
            elif function == 2:
                self.currencycalc = actualbuy / thevalue
            else:
                print('The Master Chief is an anime weeb')

            self.currencycalc = round(self.currencycalc, 2)
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
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.btcbuy.get(), 'BTC', 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : ConfirmMsgBox(self.btcbuy.get(), "BTC"))
            self.confirmbuy.grid(row=2, column=1)

        def ETH():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter ETH to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.ethbuy = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethbuy.get(), 'ETH', 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : ConfirmMsgBox(self.ethbuy, "ETH"))
            self.confirmbuy.grid(row=2, column=1)

        def XRP():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter XRP to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.xrpbuy = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpbuy.get(), 'XRP', 1))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : ConfirmMsgBox(self.xrpbuy, "XRP"))
            self.confirmbuy.grid(row=2, column=1)
        
        self.buybtcbtn = Button(self.optionwindow, text="Buy BTC", command = BTC)
        self.buybtcbtn.place(anchor = 'nw')
        self.buyethbtn = Button(self.optionwindow, text="Buy ETH", command = ETH)
        self.buyethbtn.place(anchor = 'center')
        self.buyxrpbtn = Button(self.optionwindow, text="Buy XRP", command = XRP)
        self.buyxrpbtn.place(anchor = 'ne')
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
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.btcsell.get(),'BTC', 2))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : ConfirmMsgBox(self.btcsell, "BTC"))
            self.confirmsell.grid(row=2)

        def ETH():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter ETH to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.ethsell = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethsell.get(),'ETH', 1))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : ConfirmMsgBox(self.ethsell, "ETH"))
            self.confirmsell.grid(row=2, column=1)

        def XRP():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter XRP to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.xrpsell = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpsell.get(),'XRP', 1))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : ConfirmMsgBox(self.xrpsell, "XRP"))
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


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
