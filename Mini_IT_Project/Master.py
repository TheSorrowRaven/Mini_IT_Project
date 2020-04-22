from tkinter import Tk
from GUI import GUI

# Master Class (Backbone)
class Master:

    programName = "Smart Financial Planner"

    def __init__(self):
        print("Main")
        self.LaunchApp()

    def LaunchApp(self):
        root = Tk()
        app = GUI(master = root)
        app.master.mainloop()




# Runs program
if __name__ == "__main__":
    Master = Master()
    input()

