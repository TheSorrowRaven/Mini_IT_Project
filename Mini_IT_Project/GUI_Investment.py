# Naga
from tkinter import Frame, ttk, Entry, Label, Button, Canvas, PhotoImage
from luno_python.client import Client
import Constants

class GUI_Investment:

    def __init__(self, parent: Frame):     

        user_credentials = {}

        def MainScreen():
            self.loginBtn.destroy()    #Test improper function in OOP
            pass

        def LoginMenu():
            self.investmentDesc2.destroy()
            self.proceedBtn.destroy()
            
            self.loginlabel = Label(master = parent, text = "API Key:", font = ("", 24), bg = Constants.mainWindowBgColor)
            self.loginlabel.place(x = 400, y = 420, anchor = "center")
            self.login = Entry(master = parent, textvariable ="API Key", font = ("", 24))
            self.login.place(x = 800, y = 420, anchor = "center")
            self.passwordlabel = Label(master = parent, text = "API Secret:", font = ("", 24), bg = Constants.mainWindowBgColor)
            self.passwordlabel.place(x = 390, y = 460, anchor = "center")
            self.password = Entry(master = parent, textvariable = "API Secret", font = ("", 24), show ="*")
            self.password.place(x = 800, y = 460, anchor = "center")
            self.loginBtn = Button(master = parent, text="Login", command = MainScreen)
            self.loginBtn.place(x = 1000, y = 520, anchor = "center")
            user_credentials['api_id'] = self.login
            user_credentials['api_secret'] = self.password
            self.data = Client(api_key_id= user_credentials['api_id'] , api_key_secret= user_credentials['api_secret'])

        self.investmentDesc2 = Label(master = parent, text = "Please signup first from the Luno Website", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc2.place(x = 600, y = 360, anchor = "center")
        self.proceedBtn = Button(master = parent, text="Proceed" , command = LoginMenu) #might change bg in a later date
        self.proceedBtn.place(x = 660, y = 420, anchor = "center")


    def ShowPrices(self, parent: Frame):

        pass

    def CurrentBalance(self, parent: Frame):

        pass

    #def BuyCoins(self, parent: Frame):      Planned future feature