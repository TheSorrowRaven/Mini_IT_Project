# Raven
from tkinter import Frame, label
import Constants

class GUI_Planner:

    def __init__(self, parent: Frame):
        self.plannerDesc = label(master = parent, text = "This platform all about your budget planner", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.plannerDesc.place(x = 600, y = 300, anchor = "north")
        self.plannerDesc2 = label(master = parent, text = "The safe way to double your money is to foldd it over once and put it in your pocket", font = ("", 24), bg = Constants.mainWindowBgColor)
        self.plannerDesc2.place(x = 600, y = 360, anchor = "south")
        
        pass