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
import interfaces as Interfaces
import tkinter.messagebox

class GUI_Investment(Interfaces.IOnSave):

    def OnSave(self):
        self.Main.SaveData("API Key", self.login)
        self.Main.SaveData("API Secret", self.password)


    def __init__(self, parent: Frame, main): #Attempt getting saved data and main message
        self.Main = main
        self.parent = parent
        super().__init__(main)
        self.login = main.GetSavedData("API Key")
        self.password = main.GetSavedData("API Secret")
        print('Retrieving existing login info if any')

        if (self.login is None):
            print('No login info found')
            self.investmentDesc2 = Label(master = parent, text = "Please signup first from the Luno Website", font = ("", 24), bg = Constants.mainWindowBgColor)
            self.investmentDesc2.place(x = 660, y = 360, anchor = "center")
            self.proceedBtn = Button(master = parent, text="Proceed" , command = lambda : self.LoginMenu(parent)) #might change bg in a later date
            self.proceedBtn.place(x = 660, y = 420, anchor = "center")
        
        else:
            self.LoginMenu(parent)


    def LoginMenu(self, parent: Frame): #Log in time

            def NewLogin():   #API Key info
                self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.loginlabel.place(x = 400, y = 420, anchor = "center")
                self.logino = Entry(master = parent, textvariable ="API Key", font = ("", 24))
                self.logino.place(x = 800, y = 420, anchor = "center")

            def NewPassword(): #API Key Secret
                self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
                self.passwordlabel.place(x = 390, y = 460, anchor = "center")
                self.passwordo = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
                self.passwordo.place(x = 800, y = 460, anchor = "center")

            def LoginTest(status):  #Test login before letting user log in
                self.logini = self.logino.get()
                self.passwordi = self.passwordo.get()           #Dudes saving Spartan 1337 from the dinasour maintaining his one heck of a mama reputation
                self.data = Client(api_key_id= self.logini , api_key_secret= self.passwordi)
                 
                try:
                    trial = self.data.get_balances()
                    print('Logging in....')
                    self.login = self.logini
                    self.password = self.passwordi
                    self.MainScreen(status, parent)

                except Exception as e:
                    print(e)
                    tkinter.messagebox.showerror(title="Login Error", message="Invalid api key or api key secret, please try again")

            
            if (self.login is None):
                self.investmentDesc2.destroy()
                self.proceedBtn.destroy()
                status = 0
                NewLogin()
                NewPassword()
                self.loginBtn = Button(master = parent, text="Login", command = lambda : LoginTest(status))
                self.loginBtn.place(x = 1000, y = 520, anchor = "center")

            else:
                status = 1
                self.data = Client(api_key_id= self.login , api_key_secret= self.password)
                print('Logging in...')
                self.MainScreen(status, parent)


    def MainScreen(self, status, parent: Frame):   #Main menu items
         
        #Post Login
        if status == 0:
            self.loginBtn.destroy()
            self.loginlabel.destroy()
            self.passwordlabel.destroy()
            self.logino.destroy()
            self.passwordo.destroy()

        #Display current cryptobalance
        print('Loading main screen')
        self.DropDownMenus(parent)            #problem for users with no acc    
        self.balancelabel = Label(master = parent, text="The current balance is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "nw", x = 61.0, y = 10)

        #Ensure user has a crypto wallet
        try:
            self.balancebtc = Label(master = parent, text = self.CryptoBalance(1) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balancebtc.place(anchor = "nw", x = 61.0, y = 90)
            self.btcbal = Label(master = parent, text='BTC', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.btcbal.place(anchor = 'nw', x = 210, y = 87)
            self.btcbalrm = Label(master = parent, text='RM', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.btcbalrm.place(anchor = 'nw', x = 61.0, y = 130)
            self.btcbalrmvalue = Label(master = parent, text = self.CryptoinRM(self.CryptoBalance(1),"BTC", 1), font = ("", 20), bd=1, bg = 'seashell2')
            self.btcbalrmvalue.place(anchor = 'nw', x = 120, y = 130)

        except:
            self.addaccountbtc = Label(master = parent, text='Account Unavailable', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.addaccountbtc.place(anchor = "nw", x = 61.0, y = 90)
            self.addaccountbtnbtc = Button(master = parent , text='Create BTC Account', command = lambda : self.CreateAccount(1))
            self.addaccountbtnbtc.place(anchor = "nw", x = 350 , y = 90)

        try:
            self.balanceeth = Label(master = parent, text = self.CryptoBalance(2) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balanceeth.place(anchor = "nw", x = 61.0 , y = 210)
            self.ethbal = Label(master = parent, text='ETH', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.ethbal.place(anchor = 'nw', x = 210, y = 207)
            self.ethbalrm = Label(master = parent, text='RM', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.ethbalrm.place(anchor = 'nw', x = 61.0, y = 250)
            self.ethbalrmvalue = Label(master = parent, text = self.CryptoinRM(self.CryptoBalance(2),"ETH", 1), font = ("", 20), bd=1, bg = 'seashell2')
            self.ethbalrmvalue.place(anchor = 'nw', x = 120, y = 250)

        except:
            self.addaccounteth = Label(master = parent, text='Account Unavailable', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.addaccounteth.place(anchor = "nw", x = 61.0, y = 210)
            self.addaccountbtneth = Button(master = parent , text='Create ETH Account', command = lambda : self.CreateAccount(2))
            self.addaccountbtneth.place(anchor = "nw", x = 350 , y = 210)

        try:
            self.balancexrp = Label(master = parent, text = self.CryptoBalance(3) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balancexrp.place(anchor = "nw",x = 61.0 , y = 330)
            self.xrpbal = Label(master = parent, text='XRP', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.xrpbal.place(anchor = 'nw', x = 210, y = 327)
            self.xrpbalrm = Label(master = parent, text='RM', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.xrpbalrm.place(anchor = 'nw', x = 61.0, y = 370)
            self.xrpbalrmvalue = Label(master = parent, text = self.CryptoinRM(self.CryptoBalance(3),"XRP", 1), font = ("", 20), bd=1, bg = 'seashell2')
            self.xrpbalrmvalue.place(anchor = 'nw', x = 120, y = 370)

        except:
            self.addaccountxrp = Label(master = parent, text='Account Unavailable', font = ("", 20), bg = Constants.mainWindowBgColor)
            self.addaccountxrp.place(anchor = "nw", x = 61.0, y = 330)
            self.addaccountbtnxrp = Button(master = parent , text='Create XRP Account', command = lambda : self.CreateAccount(3))
            self.addaccountbtnxrp.place(anchor = "nw", x = 350 , y = 330)


        #Display current prices
        self.balancelabel = Label(master = parent, text="The current price is :", font = ("", 26), bg = Constants.mainWindowBgColor)
        self.balancelabel.place(anchor = "nw", x = 61, y = 470)

        try:
            self.btclabel = Label(master = parent, text = 'BTC: RM', font = ("",26), bg = Constants.mainWindowBgColor)
            self.btclabel.place(anchor = 'nw', x = 61, y = 530)
            self.balancebtc1 = Label(master = parent, text = self.ShowPrice(1) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balancebtc1.place(anchor = "nw", x = 250 , y = 530)
            
        
        except:
            self.btcdisplayerror = Label(master = parent, text = 'Unable to retrieve prices', font = ("",26), bg = Constants.mainWindowBgColor)
            self.btcdisplayerror.place(anchor = 'nw', x = 61, y = 530)

        try:
            self.ethlabel = Label(master = parent, text = 'ETH: RM', font = ("",26), bg = Constants.mainWindowBgColor)
            self.ethlabel.place(anchor = 'nw', x = 61, y = 590)
            self.balanceeth1 = Label(master = parent, text = self.ShowPrice(2) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balanceeth1.place(anchor = "nw", x = 250 , y = 590)
            
        
        except:
            self.ethdisplayerror = Label(master = parent, text = 'Unable to retrieve prices', font = ("",26), bg = Constants.mainWindowBgColor)
            self.ethdisplayerror.place(anchor = 'nw', x = 61, y = 590)

        try:
            self.xrplabel = Label(master = parent, text = 'XRP: RM', font = ("",26), bg = Constants.mainWindowBgColor)
            self.xrplabel.place(anchor = 'nw', x = 61, y = 650)
            self.balancexrp1 = Label(master = parent, text = self.ShowPrice(3) ,font = ("", 20), bd =1, bg = 'seashell3')
            self.balancexrp1.place(anchor = "nw", x = 250 , y = 650)
            
        
        except:
            self.ethdisplayerror = Label(master = parent, text = 'Unable to retrieve prices', font = ("",26), bg = Constants.mainWindowBgColor)
            self.ethdisplayerror.place(anchor = 'nw', x = 61, y = 650)

        #Config Buttons
        self.configbtn = Button(master = parent, text="Manage crypto", command = self.CoinOption)
        self.configbtn.place(x = 700, y = 120, anchor = "nw")
        self.configtransc1 = Button(master = parent, text="See BTC Transactions", command = lambda: self.TransactionHistory(1))
        self.configtransc1.place(x = 700, y = 160, anchor = "nw")
        self.configtransc2 = Button(master = parent, text="See ETH transactions", command = lambda: self.TransactionHistory(2))
        self.configtransc2.place(x = 700, y = 200, anchor = "nw")
        self.configtransc3 = Button(master = parent, text="See XRP Transactions", command = lambda: self.TransactionHistory(3))
        self.configtransc3.place(x = 700, y = 240, anchor = "nw")


    def DropDownMenus(self, parent: Frame): #Choose Which account
        
        def AccountBalanceBTC(*args):
            playbtc = self.variablelolbtc.get()
            self.balancebtc.destroy()
            self.btcbalrmvalue.destroy()
            self.actualaccountbtc = self.xbtdictionary[playbtc]
            for i in self.json_datalol:
                if i['account_id'] == self.actualaccountbtc:
                    abalancebtc = i['balance']
                    self.balancebtc = Label(master = parent, text = abalancebtc ,font = ("", 20), bd =1, bg = 'seashell3')
                    self.balancebtc.place(anchor = "nw", x = 61.0, y = 90)
                    self.btcbalrmvalue = Label(master = parent, text = self.CryptoinRM(abalancebtc,"BTC", 1), font = ("", 20), bd=1, bg = 'seashell2')
                    self.btcbalrmvalue.place(anchor = 'nw', x = 120, y = 130)

        def AccountBalanceETH(*args):
            playeth = self.variableloleth.get()
            self.balanceeth.destroy()
            self.ethbalrmvalue.destroy()
            self.actualaccounteth = self.ethdictionary[playeth]
            for i in self.json_datalol:
                if i['account_id'] == self.actualaccounteth:
                    abalanceeth = i['balance']
                    self.balanceeth = Label(master = parent, text = abalanceeth ,font = ("", 20), bd =1, bg = 'seashell3')
                    self.balanceeth.place(anchor = "nw", x = 61.0 , y = 210)
                    self.ethbalrmvalue = Label(master = parent, text = self.CryptoinRM(abalanceeth,"ETH", 1), font = ("", 20), bd=1, bg = 'seashell2')
                    self.ethbalrmvalue.place(anchor = 'nw', x = 120, y = 250)

        def AccountBalanceXRP(*args):
            playxrp = self.variablelolxrp.get()
            self.balancexrp.destroy()
            self.xrpbalrmvalue.destroy()
            self.actualaccountxrp = self.xrpdictionary[playxrp]
            for i in self.json_datalol:
                if i['account_id'] == self.actualaccountxrp:
                    abalancexrp = i['balance']
                    self.balancexrp = Label(master = parent, text = abalancexrp ,font = ("", 20), bd =1, bg = 'seashell3')
                    self.balancexrp.place(anchor = "nw", x = 61.0 , y = 330)
                    self.xrpbalrmvalue = Label(master = parent, text = self.CryptoinRM(abalancexrp, "XRP", 1), font=("", 20), bd =1, bg = 'seashell2')
                    self.xrpbalrmvalue.place(anchor = 'nw', x = 120, y = 370)

        self.json_data = self.data.get_balances()
        self.json_datalol = self.json_data['balance']

        #Easy drop down access
        xbtlist = []
        ethlist = []
        xrplist = []
        xbtaccounts = []
        ethaccounts = []
        xrpaccounts = []

        n = 0
        #Segregate cryptonames and account id from lists
        for i in self.json_datalol:

            if i['asset'] == 'XBT':
                xbtaccounts.append(i['account_id'])

                try:
                    xbtlist.append(i['name'])
                except:
                    n += 1
                    xbtlist.append('noname {}'.format(n))
            
            
        for j in self.json_datalol:
            
            if j['asset'] == 'ETH':
                ethaccounts.append(j['account_id'])
                try:
                    ethlist.append(j['name'])
                except:
                    n += 1
                    ethlist.append('noname {}'.format(n))

            
        for k in self.json_datalol:

            if k['asset'] == 'XRP':
                xrpaccounts.append(k['account_id'])
                try:
                    xrplist.append(k['name'])
                except:
                    n += 1
                    xrplist.append('noname {}'.format(n))
        
        self.xbtdictionary = dict(zip(xbtlist, xbtaccounts))
        self.ethdictionary = dict(zip(ethlist, ethaccounts))
        self.xrpdictionary = dict(zip(xrplist, xrpaccounts))

        print(self.xbtdictionary)
        print(self.ethdictionary)
        print(self.xrpdictionary)

        self.variablelolbtc = StringVar(parent)
        self.variablelolbtc.set(xbtlist[0])
        self.variablelolbtc.trace("w", AccountBalanceBTC)

        self.variableloleth = StringVar(parent)
        self.variableloleth.set(ethlist[0])
        self.variableloleth.trace("w", AccountBalanceETH)

        self.variablelolxrp = StringVar(parent)
        self.variablelolxrp.set(xrplist[0])
        self.variablelolxrp.trace("w", AccountBalanceXRP)

        optionbtc = OptionMenu(parent, self.variablelolbtc, *xbtlist)
        optionbtc.place(anchor = "nw", x = 61.0 , y = 50)
        optioneth = OptionMenu(parent, self.variableloleth, *ethlist)
        optioneth.place(anchor = "nw", x = 61.0 , y = 170)
        optionxrp = OptionMenu(parent, self.variablelolxrp, *xrplist)
        optionxrp.place(anchor = "nw", x = 61.0 , y = 290)


    def CreateAccount(self, value): #Creates an account if user doesn't have one

        self.createaccountwindow = Toplevel()
        self.labelmaker = Label(self.createaccountwindow, text="Account Name: ", font=("", 20) , bg = Constants.mainWindowBgColor)
        self.labelmaker.grid(row=0)
        self.accountnameentry = Entry(self.createaccountwindow, textvariable = "Account Name", font = ("", 20))
        self.accountnameentry.grid(row=0, column=1)
        self.accountcreationbutton = Button(self.createaccountwindow, text="Create account", command = lambda : CreateAccount(value, self.accountnameentry.get()))
        self.accountcreationbutton.grid(row=1, column=1)
        def CreateAccount(value, accountname):
            if value == 1:
                try:
                    self.jsonparse = self.data.create_account('BTC', accountname)
                    tkinter.messagebox.Message("Crypto Account Progress", message= "Account Creation Successful!")
                    self.createaccountwindow.quit()

                except:
                    tkinter.messagebox.showerror("Crypto Account Progress", message = "Action Failed")
                    self.createaccountwindow.quit()

            elif value == 2:
                try:
                    self.jsonparse = self.data.create_account('ETH', accountname)
                    tkinter.messagebox.Message("Crypto Account Progress", message= "Account Creation Successful!")
                    self.createaccountwindow.quit()

                except:
                    tkinter.messagebox.showerror("Crypto Account Progress", message = "Action Failed")
                    self.createaccountwindow.quit()

            elif value == 3:
                try:
                    self.jsonparse = self.data.create_account('XRP', accountname)
                    tkinter.messagebox.Message("Crypto Account Progress", message= "Account Creation Successful!")
                    self.createaccountwindow.quit()

                except:
                    tkinter.messagebox.showerror("Crypto Account Progress", message = "Action Failed")
                    self.createaccountwindow.quit()


    def TransactionHistory(self, value):       #Get transaction history
        self.json_data = self.data.get_balances()
        self.json_data = self.json_data['balance']

        self.transactionwindow = Toplevel()

        if value == 1:
            for i in self.json_data:
                if i['asset'] == 'XBT':
                    idinfo = i['account_id']

        if value == 2:
            for i in self.json_data:
                if i['asset'] == 'ETH':
                        idinfo = i['account_id']

        elif value == 3:
            for i in self.json_data:
                if i['asset'] == 'XRP':
                        idinfo = i['account_id']

        min_row = -100
        max_row = 0
        transactionlist = self.data.list_transactions(idinfo, max_row, min_row)
        print(transactionlist)
        def TransactionIndex():

            try:
                self.transactioninfo = Label(self.transactionwindow, text = "{} :".format(transactionlist['transactions'][0]['row_index']), font = ("",26), bg = Constants.mainWindowBgColor)
                self.transactioninfo.grid(row=0)
                self.transactioninfo1 = Label(self.transactionwindow, text = transactionlist['transactions'][0]['description'], font = ("",26), bg = Constants.mainWindowBgColor)
                self.transactioninfo1.grid(row=0, column = 1)

            except:
                tkinter.messagebox.showerror("Transaction", "No transactions recorded")
                self.transactionwindow.destroy()
        TransactionIndex()
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


    def CryptoinRM(self, buysell, crypto, value):      #Display coin value in RM
 
        try:

            actualbuy = float(buysell)
            print('ok1')

            if crypto == 'BTC':
                thevalue = self.ShowPrice(1)

            elif crypto == 'ETH':
                thevalue = self.ShowPrice(2)

            elif crypto == 'XRP':
                thevalue = self.ShowPrice(3)

            thefloat = float(thevalue)
            self.currencycalc = actualbuy * thefloat
            self.currencycalc = round(self.currencycalc, 2)
            
            if value == 1:
                return self.currencycalc        #Return ringgit value  

            elif value == 2:         #return
                self.textdisplay = "RM {}" 
                self.actualtextdisplay = self.textdisplay.format(self.currencycalc)
                try:
                    self.currencydisplay.destroy()        #Don't edit out !!!
                except:
                    pass
                self.currencydisplay = Label(self.optionwindow, text = self.actualtextdisplay, font = ("", 26), bg = Constants.mainWindowBgColor)
                self.currencydisplay.grid(row=1, column=1)
      
            
        except:
            tkinter.messagebox.showerror("Crypto Manager", "Invalid input")


    def RMinCrypto(self, value, crypto):                       #Display RM value in coin
        try:
            valuefloat = float(value)
            print(valuefloat)
            if crypto == 'BTC':
                price = self.ShowPrice(1)
                pricefloat = float(price)
                print(pricefloat)
                self.totalbtc = round(valuefloat / pricefloat, 6)
                self.viewbuybtc = Label(self.optionwindow, text = "{} BTC".format(self.totalbtc), font=("", 20))
                self.viewbuybtc.grid(row = 5, column = 1)

            elif crypto == 'ETH':
                price = self.ShowPrice(2)
                pricefloat = float(price)
                self.totaleth = round(valuefloat / pricefloat, 6)
                self.viewbuyeth = Label(self.optionwindow, text = "{} ETH".format(self.totaleth), font=("", 20))
                self.viewbuyeth.grid(row = 5, column = 1)

            elif crypto == 'XRP':
                price = self.ShowPrice(3)
                pricefloat = float(price)
                self.totalxrp = round(valuefloat / pricefloat, 6)
                self.viewbuyeth = Label(self.optionwindow, text = "{} XRP".format(self.totalxrp), font=("", 20))
                self.viewbuyeth.grid(row = 5, column = 1)
        
        except:
            tkinter.messagebox.showerror("Crypto Manager", "Invalid input")


    def BuyCoins(self):

        self.buy.destroy()
        self.sell.destroy()

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
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.btcbuy.get(), 'BTC', 2))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.btcbuy.get(), "BTC", 1))
            self.confirmbuy.grid(row=2, column=1)
            
            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3) #Buy in ringgit instead

            self.buylabelrm = Label(self.optionwindow, text='Enter RM to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabelrm.grid(row=4)
            self.btcbuyrm = Entry(self.optionwindow, textvariable ="Total RM", font = ("", 24))
            self.btcbuyrm.grid(row=4, column=1)
            self.viewbuyabtc = Button(self.optionwindow, text = 'Total BTC', command = lambda : self.RMinCrypto(self.btcbuyrm.get(), 'BTC'))
            self.viewbuyabtc.grid(row=5)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.totalbtc, "BTC", 1))
            self.confirmbuy.grid(row=6, column=1)


        def ETH():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter ETH to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.ethbuy = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethbuy.get(), 'ETH', 2))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.ethbuy.get(), "ETH", 1))
            self.confirmbuy.grid(row=2, column=1)
            
            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3)

            self.buylabelrm = Label(self.optionwindow, text='Enter RM to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabelrm.grid(row=4)
            self.ethbuyrm = Entry(self.optionwindow, textvariable ="Total RM", font = ("", 24))
            self.ethbuyrm.grid(row=4, column=1)
            self.viewbuyaeth = Button(self.optionwindow, text = 'Total ETH', command = lambda : self.RMinCrypto(self.ethbuyrm.get(), 'ETH'))
            self.viewbuyaeth.grid(row=5)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.totaleth, "ETH", 1))
            self.confirmbuy.grid(row=6, column=1)


        def XRP():
            FunctionDestroyer()
            self.buylabel = Label(self.optionwindow, text='Enter XRP to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabel.grid(row=0)
            self.xrpbuy = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpbuy.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpbuy.get(), 'XRP', 2))
            self.viewbuy.grid(row=1)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.xrpbuy.get(), "XRP", 1))
            self.confirmbuy.grid(row=2, column=1)

            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3)

            self.buylabelrm = Label(self.optionwindow, text='Enter RM to buy: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.buylabelrm.grid(row=4)
            self.xrpbuyrm = Entry(self.optionwindow, textvariable ="Total RM", font = ("", 24))
            self.xrpbuyrm.grid(row=4, column=1)
            self.viewbuyaxrp = Button(self.optionwindow, text = 'Total XRP', command = lambda : self.RMinCrypto(self.xrpbuyrm.get(), 'XRP'))
            self.viewbuyaxrp.grid(row=5)
            self.confirmbuy = Button(self.optionwindow, text="Confirm Purchase", command = lambda : self.ConfirmMsgBox(self.totalxrp, "XRP", 1))
            self.confirmbuy.grid(row=6, column=1)

        
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
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.btcsell.get(), "BTC", 2))
            self.confirmsell.grid(row=2)
            
            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3)

            self.selllabelrm = Label(self.optionwindow, text='Enter RM of sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabelrm.grid(row=4)
            self.btcsellrm = Entry(self.optionwindow, textvariable ="Total RMsell", font = ("", 24))
            self.btcsellrm.grid(row=4, column=1)
            self.viewsellabtc = Button(self.optionwindow, text = 'Total BTC', command = lambda : self.RMinCrypto(self.btcsellrm.get(), 'BTC'))
            self.viewsellabtc.grid(row=5)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.totalbtc, "BTC", 2))
            self.confirmsell.grid(row=6, column=1)

        def ETH():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter ETH to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.ethsell = Entry(self.optionwindow, textvariable ="Total ETH", font = ("", 24))
            self.ethsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.ethsell.get(),'ETH', 2))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.ethsell.get(), "ETH", 2))
            self.confirmsell.grid(row=2, column=1)
            
            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3)

            self.selllabelrm = Label(self.optionwindow, text='Enter RM of sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabelrm.grid(row=4)
            self.ethsellrm = Entry(self.optionwindow, textvariable ="Total RMsell", font = ("", 24))
            self.ethsellrm.grid(row=4, column=1)
            self.viewsellaeth = Button(self.optionwindow, text = 'Total ETH', command = lambda : self.RMinCrypto(self.ethsellrm.get(), 'ETH'))
            self.viewsellaeth.grid(row=5)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.totaleth, "ETH", 2))
            self.confirmsell.grid(row=6, column=1)

        def XRP():
            FunctionDestroyer()
            self.selllabel = Label(self.optionwindow, text='Enter XRP to sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabel.grid(row=0)
            self.xrpsell = Entry(self.optionwindow, textvariable ="Total XRP", font = ("", 24))
            self.xrpsell.grid(row=0, column=1)
            self.viewbuy = Button(self.optionwindow, text="View Currency in RM: ", command = lambda : self.CryptoinRM(self.xrpsell.get(),'XRP', 2))
            self.viewbuy.grid(row=1)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.xrpsell.get(), "XRP", 2))
            self.confirmsell.grid(row=2, column=1)
            
            self.oroption = Label(self.optionwindow, text='Or: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.oroption.grid(row=3)

            self.selllabelrm = Label(self.optionwindow, text='Enter RM of sell: ', font = ("", 26), bg = Constants.mainWindowBgColor)
            self.selllabelrm.grid(row=4)
            self.xrpsellrm = Entry(self.optionwindow, textvariable ="Total RMsell", font = ("", 24))
            self.xrpsellrm.grid(row=4, column=1)
            self.viewsellaxrp = Button(self.optionwindow, text = 'Total XRP', command = lambda : self.RMinCrypto(self.xrpsellrm.get(), 'XRP'))
            self.viewsellaxrp.grid(row=5)
            self.confirmsell = Button(self.optionwindow, text="Confirm Sell", command = lambda : self.ConfirmMsgBox(self.totalxrp, "XRP", 2))
            self.confirmsell.grid(row=6, column=1)

        self.sellbtcbtn = Button(self.optionwindow, text="Sell BTC", command = BTC)
        self.sellbtcbtn.place(anchor = 'nw')
        self.sellethbtn = Button(self.optionwindow, text="Sell ETH", command = ETH)
        self.sellethbtn.place(anchor = 'center')
        self.sellxrpbtn = Button(self.optionwindow, text="Sell XRP", command = XRP)
        self.sellxrpbtn.place(anchor = 'ne')
        self.sellbtcbtn.pack()
        self.sellethbtn.pack()
        self.sellxrpbtn.pack()


    def ConfirmMsgBox(self, value, crypto, buysell):

        def ActualMessageBox(value, crypto, function):
            if function == 1:
                self.MsgBox = tkinter.messagebox.askquestion ('Crypto Coin Manager',"Would you like to proceed with transaction of {} {}?".format(value, crypto),icon = 'warning')
                return self.MsgBox
            
            elif function == 2:
                self.MsgBoxexit = tkinter.messagebox.showinfo('Crypto Coin Manager', "Transaction Succesful!")

            elif function == 3:
                self.MsgBoxError = tkinter.messagebox.showerror('Cryto Coin Manager', "Insufficient balance or permissions, please try again")

        if crypto == 'BTC':
            try:
                msg = ActualMessageBox(value, crypto, 1)
                if msg == 'yes':
                    if buysell == 1:
                        self.infobuy = self.data.create_quote(value, 'XBTMYR', 'BUY')
                        self.infobuy = self.infobuy['id']
                        print(self.infobuy)
                        self.quoteexercise = self.data.exercise_quote(self.infobuy)
                        ActualMessageBox(value, crypto, 2)
                    elif buysell == 2:
                        self.infosell = self.data.create_quote(value, 'MYRXBT', 'SELL')
                        self.infosell = self.infosell['id']
                        print(self.infosell)
                        self.quoteexercise = self.data.exercise_quote(self.infosell)
                        ActualMessageBox(value, crypto, 2)
            
            except:
                ActualMessageBox(value, crypto, 3)

        elif crypto == 'ETH':
            try:
                msg = ActualMessageBox(value, crypto, 1)
                if msg == 'yes':
                    if buysell == 1:
                        self.infobuy = self.data.create_quote(value, 'ETHMYR', 'BUY')
                        self.infobuy = self.infobuy['id']
                        print(self.infobuy)
                        self.quoteexercise = self.data.exercise_quote(self.infobuy)
                        ActualMessageBox(value, crypto, 2)
                    elif buysell == 2:
                        self.infosell = self.data.create_quote(value, 'ETHMYR', 'SELL')
                        self.infosell = self.infosell['id']
                        print(self.infosell)
                        self.quoteexercise = self.data.exercise_quote(self.infosell)
                        ActualMessageBox(value, crypto, 2)
                
            except:
                ActualMessageBox(value, crypto, 3)

        elif crypto == 'XRP':
            try:
                msg = ActualMessageBox(value, crypto, 1)
                if msg == 'yes':

                    if buysell == 1:
                        self.infobuy = self.data.create_quote(value, 'XRPMYR', 'BUY')
                        self.infobuy = self.infobuy['id']
                        print(self.infobuy)
                        self.quoteexercise = self.data.exercise_quote(self.infobuy)
                        ActualMessageBox(value, crypto, 2)

                    elif buysell == 2:
                        self.infosell = self.data.create_quote(value, 'XRPMYR', 'SELL')
                        self.infosell = self.infosell['id']
                        print(self.infosell)
                        self.quoteexercise = self.data.exercise_quote(self.infosell)
                        ActualMessageBox(value, crypto, 2)
            
            except Exception as e:
                print(e)
                ActualMessageBox(value, crypto, 3)



if __name__ == "__main__":
    print("Please run main.py instead")
    pass
