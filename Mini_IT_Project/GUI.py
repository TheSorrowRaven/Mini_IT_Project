from tkinter import Frame
import Constants

class GUI(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title(Constants.projectDisplayTitle)
        self.master.geometry("750x500")
        self.master.resizable(False, False)
        self.configure(background = "white")
        self.pack(fill="both", expand=1)

