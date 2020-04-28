from tkinter import Tk
from GUI import GUI

# Master Class (Backbone)
class Master:

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
    input() # Catches a blank input for debugging

