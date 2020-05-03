# Raven
from tkinter import Frame, Label
import Constants

class GUI_Planner:

    def __init__(self, parent: Frame):
        self.plannerDesc = Label(master = parent, text = "This platform all about your budget planner", font = ("", 12), bg = Constants.mainWindowBgColor)
        self.plannerDesc.place(relx = 0.5 , rely = 5, anchor = "n")
        self.plannerDesc2 = Label(master = parent, text = "\'The safe way to double your money is to fold it over once and put it in your pocket\'", font = ("", 12), bg = Constants.mainWindowBgColor)
        self.plannerDesc2.place(relx = 0, rely = 1.0, anchor = "se")
        
        pass