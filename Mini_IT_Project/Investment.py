# Raven
from tkinter import Frame, Label, Button, Canvas, PhotoImage
import Constants

class Investment:

    def __init__(self, parent: Frame):
        self.investmentDesc = Label(master = parent, text = "InvestmentERROR", font = ("", 36), bg = Constants.mainWindowBgColor)
        self.investmentDesc.place(anchor = "center")
        

        pass