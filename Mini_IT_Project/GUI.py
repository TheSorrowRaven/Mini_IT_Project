# Raven
from tkinter import Frame, Label, Button, Canvas, PhotoImage
from PIL import Image, ImageTk
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
        
        self.buttonInitial = ImageTk.PhotoImage(Image.open("Assets/Button_Initial.png"))
        self.buttonHover   = ImageTk.PhotoImage(Image.open("Assets/Button_Hover.png"))
        self.buttonDown    = ImageTk.PhotoImage(Image.open("Assets/Button_Down.png"))

        buttonPaths = [ "Assets/Button_Planner_Initial.png", "Assets/Button_Account_Initial.png", "Assets/Button_Investment_Initial.png", "Assets/Button_Quit_Initial.png",
                        "Assets/Button_Planner_Hover.png"  , "Assets/Button_Account_Hover.png"  , "Assets/Button_Investment_Hover.png"  , "Assets/Button_Quit_Hover.png",
                        "Assets/Button_Planner_Down.png"   , "Assets/Button_Account_Down.png"   , "Assets/Button_Investment_Down.png"   , "Assets/Button_Quit_Down.png"]

        self.initialButtons = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(0                    , len(buttonPaths)//3)]
        self.hoverButtons   = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(len(buttonPaths)//3  , len(buttonPaths)//3*2)]
        self.downButtons    = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(len(buttonPaths)//3*2, len(buttonPaths))]
        
        plannerButton = Button(master = self.master, command = lambda: print("Planner"))
        accountButton = Button(master = self.master, command = lambda: print("Account"))
        investButton  = Button(master = self.master, command = lambda: print("Investment"))
        quitButton    = Button(master = self.master, command = lambda: print("Quit"))

        plannerButton.place(x = 640, y = Constants.firstButtonYVal, anchor = "nw")
        accountButton.place(x = 700, y = Constants.firstButtonYVal + Constants.nextButtonYDiff, anchor = "nw")
        investButton.place (x = 760, y = Constants.firstButtonYVal + Constants.nextButtonYDiff * 2, anchor = "nw")
        quitButton.place   (x = 1060, y = Constants.firstButtonYVal + Constants.nextButtonYDiff * 3, anchor = "nw")

        updatedButtons = [plannerButton, accountButton, investButton, quitButton]

        def SetButton(button, targetImage):
            button.configure(image = targetImage, background = Constants.mainWindowBgColor)

        for i in range(len(updatedButtons)):
            updatedButtons[i].configure(borderwidth = 0, highlightthickness = 0, background = Constants.mainWindowBgColor, activeforeground = Constants.mainWindowBgColor, activebackground = Constants.mainWindowBgColor)

            butt = updatedButtons[i]
            SetButton(butt, self.initialButtons[i])

            updatedButtons[i].bind("<Leave>",           lambda x, butt = butt, i = i: SetButton(butt, self.initialButtons[i]))
            updatedButtons[i].bind("<Enter>",           lambda x, butt = butt, i = i: SetButton(butt, self.hoverButtons[i]))
            updatedButtons[i].bind("<ButtonPress>",     lambda x, butt = butt, i = i: SetButton(butt, self.downButtons[i]))
            updatedButtons[i].bind("<ButtonRelease>",   lambda x, butt = butt, i = i: SetButton(butt, self.initialButtons[i]))

        statusFrame = Frame(master = self.master, width = 460, height = 320, background = "black")
        statusFrame.place(x = 80, y = 80, anchor = "nw")



        self.AppendListToWidgets(updatedButtons)
        self.AppendListToWidgets([updatedButtons])

        self.currentSubWindow = Constants.mainMenuSub
        pass

    def GoToPlanner(self):
        self.Main.Warn()
        self.EmptyWindow()
        pass

