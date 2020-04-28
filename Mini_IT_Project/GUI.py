# Raven
from tkinter import Frame, Label, Button
import Constants
import Functions


# GUI
# 1. EmptyWindow
# 2. Set widgets
# 3. AppendListToWidgets
# 4. Place/pack widgets
    

class GUI(Frame):

    widgets = [] # Contains all UI elements
    currentWindow = None
    currentSubWindow = None

    def __init__(self, Main, master = None, window: str = Constants.mainWindow):
        super().__init__(master)
        self.master = master
        self.Main = Main

        Functions.Switch([Constants.mainWindow, Constants.warningWindow, Constants.queryWindow], 
        [self.InitMainWindow, self.InitWarnWindow, self.InitQueryWindow, 
        lambda: self.Raise(Exception("No such window exists")) ], window)
    
    def Raise(self, exception):
        raise exception
        
# Window Functions
    def GetCurrentWindow(self) -> str:
        if (self.currentSubWindow is not None):
            return self.currentWindow + " - " + self.currentSubWindow
        else:
            return self.currentWindow

    def EmptyWindow(self):
        for i in self.widgets:
            i.destroy()

    def AppendListToWidgets(self, list):
        for i in list:
            self.widgets.append(i)


# Main windows
    def InitQueryWindow(self):

        pass

    def InitWarnWindow(self):
        self.master.title(Constants.warningDisplayTitle)
        self.master.geometry(Constants.warningWindowSize)
        self.master.resizable(False, False)
        self.configure(background = Constants.warningWindowBgColor)
        self.pack(fill="both", expand = 1)
    
    def InitMainWindow(self):
        self.master.title(Constants.mainDisplayTitle)
        self.master.geometry(Constants.mainWindowSize)
        self.master.resizable(False, False)
        self.configure(background = Constants.mainWindowBgColor)
        self.pack(fill="both", expand = 1)
        self.currentWindow = Constants.mainWindow
        self.MainMenu()


# Main window Sub windows
    def MainMenu(self):
        self.EmptyWindow()

        label1 = Label(master = self.master, text = "Hi")
        label2 = Label(master = self.master, text = "BOOo")
        button1 = Button(master = self.master, text = "Click me", command = self.GoToPlanner)

        self.AppendListToWidgets([label1, label2, button1])

        label1.place(relx = 0.5, rely = 0.5)
        button1.place(relx = 0.5, rely = 0.6)
        self.currentSubWindow = Constants.mainMenuSub
        pass

    def GoToPlanner(self):
        self.Main.Warn()
        self.EmptyWindow()
        pass

