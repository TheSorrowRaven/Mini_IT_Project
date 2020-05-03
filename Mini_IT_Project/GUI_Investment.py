# Raven
from tkinter import Frame, Label, Button, Canvas, PhotoImage
import Constants

class GUI_Investment:

    def __init__(self, parent: Frame):
        self.investmentDesc = Label(master = parent, text = "NOTE: If you don't have a Luno Account", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc.place(x = 600, y = 300, anchor = "center")
        self.investmentDesc2 = Label(master = parent, text = "Please signup first from the Luno Website", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.investmentDesc2.place(x = 600, y = 365, anchor = "center")

        

        pass