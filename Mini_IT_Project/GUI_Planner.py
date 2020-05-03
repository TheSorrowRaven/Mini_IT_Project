# Raven
from tkinter import Frame, Label
import Constants

class GUI_Planner:

    def __init__(self, parent: Frame):
        self.plannerDesc = Label(master = parent, text = "This platform all about your budget planner", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.plannerDesc.place(relx = 100 , rely = 100, anchor = "n")
        self.plannerDesc2 = Label(master = parent, text = "The safe way to double your money is to foldd it over once and put it in your pocket", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.plannerDesc2.place(relx = 0, rely = 0, anchor = "nw")
        
        pass