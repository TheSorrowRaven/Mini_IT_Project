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
        app = GUI.GUI(self, master = root, window = Constants.mainWindow)
        app.master.mainloop()

    def Warn(self):
        queryWindow = Tk()
        query = GUI.GUI(self, master = queryWindow, window = Constants.warningWindow)
        query.master.mainloop()
        pass

    def Query(self):
        queryWindow = Tk()
        query = GUI.GUI(self, master = queryWindow, window = Constants.warningWindow)
        query.master.mainloop()
        pass


# Runs program
if __name__ == "__main__":
    master = Master()
    master.LaunchApp()
    #input() # Catches a blank input for debugging


