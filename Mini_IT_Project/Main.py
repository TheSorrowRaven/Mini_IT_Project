# Raven
import Constants
from tkinter import Tk

import GUI
import Rick
import Interfaces

# Master Class (Backbone)
class Master:


    def __init__(self):

        # Initialize IO
        self.IO = Rick.Pickler(Constants.saveFile)
        self.IO.UnpickleJar()

        # Make sure this runs
        print("Main")
        
    def GetSavedData(self, key):
        if (key in self.IO.pickles):
            return self.IO.pickles[key]
        else:
            return None
            
    def SaveData(self, key, data):
        self.IO.TurnToPickle(key, data)

    def LaunchApp(self):
        self.root = Tk()
        self.a = 0
        self.root.protocol("WM_DELETE_WINDOW", self.SaveAll)
        app = GUI.GUI(self, root = self.root, window = Constants.mainWindow)
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

    saveEvents = []
    loadEvents = []

    def ExitRoot(self):
        self.SaveAll()
        self.root.quit()

    def SaveAll(self):
        for i in self.saveEvents:
            i.OnSave()
        self.IO.PickleIntoJar()

    def AddSaveEvent(self, IOnSave):
        self.saveEvents.append(IOnSave)
    def AddLoadEvent(self, IOnLoad):
        self.loadEvents.append(IOnLoad)

# Runs program
if __name__ == "__main__":
    master = Master()
    master.LaunchApp()
    #input() # Catches a blank input for debugging


