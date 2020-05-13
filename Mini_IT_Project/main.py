###
#/***************************************************
#File Name: main.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###
from tkinter import Tk

import constants as Constants
import gui as GUI
import rick as Rick
import interfaces as Interfaces

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
        self.root.protocol("WM_DELETE_WINDOW", self.ExitRoot)
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
        print("Save Call")
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


