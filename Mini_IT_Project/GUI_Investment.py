# Naga
from tkinter import Frame, Label, Button, Canvas, PhotoImage
import Constants

class GUI_Investment:

    def __init__(self, parent: Frame):
        self.investmentDesc = Label(master = parent, text = "NOTE: If you don't have a Luno Account", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc.place(x = 600, y = 300, anchor = "center")
        self.investmentDesc2 = Label(master = parent, text = "Please signup first from the Luno Website", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc2.place(x = 600, y = 360, anchor = "center")
        self.proceedBtn = Button(master = parent, text = "Proceed", font = ("", 24), bg = Constants.mainWindowBgColor) #might change bg in a later date
        self.proceedBtn.place(x = 660, y = 420, anchor = "center")
        pass

    def LoginMenu(self, parent: Frame):

        pass

    def MainScreen(self, parent: Frame):

        pass

    def ShowPrices(self, parent: Frame):

        pass

    def CurrentBalance(self, parent: Frame):

        pass

    #def BuyCoins(self, parent: Frame):      Planned future feature

