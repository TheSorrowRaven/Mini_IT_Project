# Raven
import Constants
from tkinter import Tk

import GUI

# Master Class (Backbone)
class Master:


    def __init__(self):
        print("Main")
        

    def LaunchApp(self):
        root = Tk()
        app = GUI.GUI(self, root = root, window = Constants.mainWindow)
        app.root.mainloop()

    def Warn(self):
        queryWindow = Tk()
        query = GUI.GUI(self, root = queryWindow, window = Constants.warningWindow)
        query.root.mainloop()
        pass

    def Query(self):
        queryWindow = Tk()
        query = GUI.GUI(self, root = queryWindow, window = Constants.warningWindow)
        query.root.mainloop()
        pass


# Runs program
if __name__ == "__main__":
    master = Master()
    master.LaunchApp()
    #input() # Catches a blank input for debugging


