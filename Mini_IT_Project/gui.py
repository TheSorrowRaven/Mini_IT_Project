# Raven
from tkinter import Frame, Label, Button, Canvas, PhotoImage
from PIL import Image, ImageTk
import constants as Constants
import functions as Functions

import gui_planner as GUI_Planner
import gui_account as GUI_Account
import gui_investment as GUI_Investment

# GUI
# 1. EmptyWindow
# 2. Set widgets
# 3. AppendListToWidgets
# 4. Place/pack widgets
    

class GUI(Frame):

    currentWindow = None
    currentSubWindow = None

    def __init__(self, Main, root = None, window: str = Constants.mainWindow):
        super().__init__(root)
        self.root = root
        self.Main = Main

        def Raise(exception):
            raise exception
        Functions.Switch([Constants.mainWindow, Constants.warningWindow, Constants.queryWindow], 
        [self.InitMainWindow, self.InitWarnWindow, self.InitQueryWindow, 
        lambda: Raise(Exception("No such window exists")) ], window)
    
        
# Window Functions
    def GetCurrentWindow(self) -> str:
        if (self.currentSubWindow is not None):
            return self.currentWindow + " - " + self.currentSubWindow
        else:
            return self.currentWindow

    def HideLastWindow(self):
        global container

        def SetContainer(frame: Frame):
            global container
            container = frame

        Functions.Switch(
            [Constants.mainWindow, Constants.warningWindow, Constants.queryWindow],
            [lambda: Functions.Switch(   
                [Constants.mainMenuSub, Constants.plannerSub, Constants.accountSub, Constants.investmentSub],
                [   lambda: SetContainer(self.mainMenuFrame), 
                    lambda: SetContainer(self.plannerFrame), 
                    lambda: SetContainer(self.accountFrame), 
                    lambda: SetContainer(self.investmentFrame), 
                lambda: SetContainer(None)], self.currentSubWindow
            ), 
            lambda: print(None), lambda: print(None), 
            lambda: print("Non existent")], self.currentWindow
        )

        if (container is not None):
            container.pack_forget()


# Main windows
    def InitQueryWindow(self):

        pass

    def InitWarnWindow(self):
        self.root.title(Constants.warningDisplayTitle)
        self.root.geometry(Constants.warningWindowSize)
        self.root.resizable(False, False)
        self.configure(background = Constants.warningWindowBgColor)
        self.pack(fill = "both" , expand = 1)
    
    def InitMainWindow(self):
        self.root.title(Constants.mainDisplayTitle)
        self.root.geometry(Constants.mainWindowSize)
        self.root.resizable(False, False)
        self.configure(background = Constants.mainWindowBgColor)
        self.pack(fill = "both" , expand = 1)

        self.mainWindowFrame = Frame(master = self)
        self.mainWindowFrame.configure(background = Constants.mainWindowBgColor)
        self.mainWindowFrame.pack(fill = "both", expand = 1)

        self.currentWindow = Constants.mainWindow

        self.InitMainMenu  (self.mainWindowFrame)
        self.InitPlanner   (self.mainWindowFrame)
        self.InitAccount   (self.mainWindowFrame)
        self.InitInvestment(self.mainWindowFrame)
        self.InitNavBar    (self.mainWindowFrame)

        # Boot Main Menu as first page for Main Window as default
        self.MainMenu(self.mainMenuFrame)


# Main window Sub windows
    def InitMainMenu(self, parent: Frame):

        self.mainMenuFrame = Frame(master = parent)
        self.mainMenuFrame.configure(background = Constants.mainWindowBgColor)
        parent = self.mainMenuFrame

        self.buttonInitial = ImageTk.PhotoImage(Image.open("Assets/Button_Initial.png"))
        self.buttonHover   = ImageTk.PhotoImage(Image.open("Assets/Button_Hover.png"))
        self.buttonDown    = ImageTk.PhotoImage(Image.open("Assets/Button_Down.png"))

        buttonPaths = [ "Assets/Button_Planner_Initial.png", "Assets/Button_Account_Initial.png", "Assets/Button_Investment_Initial.png", "Assets/Button_Quit_Initial.png",
                        "Assets/Button_Planner_Hover.png"  , "Assets/Button_Account_Hover.png"  , "Assets/Button_Investment_Hover.png"  , "Assets/Button_Quit_Hover.png",
                        "Assets/Button_Planner_Down.png"   , "Assets/Button_Account_Down.png"   , "Assets/Button_Investment_Down.png"   , "Assets/Button_Quit_Down.png"]

        self.initialButtons = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(0                    , len(buttonPaths)//3)]
        self.hoverButtons   = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(len(buttonPaths)//3  , len(buttonPaths)//3*2)]
        self.downButtons    = [ImageTk.PhotoImage(Image.open(buttonPaths[i])) for i in range(len(buttonPaths)//3*2, len(buttonPaths))]
        
        self.plannerButton = Button(master = parent, command = lambda: self.Planner(self.plannerFrame))
        self.accountButton = Button(master = parent, command = lambda: self.Account(self.accountFrame))
        self.investButton  = Button(master = parent, command = lambda: self.Investment(self.investmentFrame))
        self.quitButton    = Button(master = parent, command = lambda: self.Main.ExitRoot())

        self.plannerButton.place(x = 640, y = Constants.firstButtonYVal, anchor = "nw")
        self.accountButton.place(x = 740, y = Constants.firstButtonYVal + Constants.nextButtonYDiff, anchor = "nw")
        self.investButton.place (x = 840, y = Constants.firstButtonYVal + Constants.nextButtonYDiff * 2, anchor = "nw")
        self.quitButton.place   (x = 1060, y = Constants.firstButtonYVal + Constants.nextButtonYDiff * 3, anchor = "nw")

        updatedButtons = [self.plannerButton, self.accountButton, self.investButton, self.quitButton]

        def SetButton(button, targetImage):
            button.configure(image = targetImage, background = Constants.mainWindowBgColor)

        for i in range(len(updatedButtons)):
            updatedButtons[i].configure(borderwidth = 0, highlightthickness = 0, background = Constants.mainWindowBgColor, activeforeground = Constants.mainWindowBgColor, activebackground = Constants.mainWindowBgColor)

            butt = updatedButtons[i]
            SetButton(butt, self.initialButtons[i])

            updatedButtons[i].bind("<Leave>",         lambda x, butt = butt, i = i: SetButton(butt, self.initialButtons[i]))
            updatedButtons[i].bind("<Enter>",         lambda x, butt = butt, i = i: SetButton(butt, self.hoverButtons[i]))
            updatedButtons[i].bind("<ButtonPress>",   lambda x, butt = butt, i = i: SetButton(butt, self.downButtons[i]))
            updatedButtons[i].bind("<ButtonRelease>", lambda x, butt = butt, i = i: SetButton(butt, self.initialButtons[i]))

        self.statusFrame = Frame(master = parent, bg = Constants.mainWindowBgColor)
        self.statusFrame.place(x = 80, y = 80, anchor = "nw")
        self.statusLabel = Label(master = self.statusFrame, text = "Smart Financial Planner", font = ("Comic Sans MS", 48),bg = Constants.mainWindowBgColor)
        self.statusLabel.pack()

    def InitPlanner(self, parent: Frame):

        self.plannerFrame = Frame(master = parent)
        self.plannerFrame.configure(background = Constants.mainWindowBgColor)
        parent = self.plannerFrame

        self.plannerContainer = Frame(master = parent, bg = Constants.mainWindowBgColor, width = 1280-54, height = 720)
        self.plannerContainer.place(x = 54, y = 0, anchor = "nw")

        self.plannerTitle = Label(master = self.plannerFrame, text = "Planner", font = ("", 36), bg = Constants.mainWindowBgColor)
        self.plannerTitle.place(x = 55, y = 0, anchor = "nw")

        self.planner = GUI_Planner.GUI_Planner(parent, self.Main)

    def InitAccount(self, parent: Frame):

        self.accountFrame = Frame(master = parent)
        self.accountFrame.configure(background = Constants.mainWindowBgColor)
        parent = self.accountFrame
        
        self.accountContainer = Frame(master = parent, bg = Constants.mainWindowBgColor, width = 1280-54, height = 720)
        self.accountContainer.place(x = 54, y = 0, anchor = "nw")

        self.accountTitle = Label(master = self.accountFrame, text = "Account", font = ("", 36), bg = Constants.mainWindowBgColor)
        self.accountTitle.place(x = 55, y = 0, anchor = "nw")

        self.account = GUI_Account.GUI_Account(parent, self.Main)

    def InitInvestment(self, parent: Frame):

        self.investmentFrame = Frame(master = parent)
        self.investmentFrame.configure(background = Constants.mainWindowBgColor)
        parent = self.investmentFrame

        self.investmentContainer = Frame(master = parent, bg = Constants.mainWindowBgColor, width = 1280-54, height = 720)
        self.investmentContainer.place(x = 54, y = 0, anchor = "nw")

        self.investmentTitle = Label(master = self.investmentFrame, text = "Investment", font = ("", 36), bg = Constants.mainWindowBgColor)
        self.investmentTitle.place(x = 55, y = 0, anchor = "nw")

        self.investment = GUI_Investment.GUI_Investment(parent, self.Main)

    def InitNavBar(self, parent: Frame):
        
        self.navBarFrame = Frame(master = parent)
        self.navBarFrame.configure(height = 720, width = 54, bg = Constants.navBarColor)
        self.navBarFrame.pack_propagate(0)

        self.navButtonContainer = Frame(master = self.navBarFrame, bg = Constants.navBarColor)
        self.navButtonContainer.place(relx = 0, rely = 0, anchor = "nw")

        self.backIcon       = ImageTk.PhotoImage(Image.open("Assets/Icon_Back.png"))
        self.plannerIcon    = ImageTk.PhotoImage(Image.open("Assets/Icon_Planner.png"))
        self.accountIcon    = ImageTk.PhotoImage(Image.open("Assets/Icon_Account.png"))
        self.investmentIcon = ImageTk.PhotoImage(Image.open("Assets/Icon_Investment.png"))

        self.mainMenuNavButton    = Button(master = self.navButtonContainer, command = lambda: self.MainMenu(self.mainMenuFrame), 
                                          width = 50, bg = Constants.navBarColor, highlightthickness = 0, 
                                          activeforeground = Constants.navBarColor, activebackground = Constants.navBarColor, image = self.backIcon)
        self.plannerNavButton    = Button(master = self.navButtonContainer, command = lambda: self.Planner(self.plannerFrame),
                                          width = 50, bg = Constants.navBarColor,  highlightthickness = 0, 
                                          activeforeground = Constants.navBarColor, activebackground = Constants.navBarColor, image = self.plannerIcon)

        self.accountNavButton    = Button(master = self.navButtonContainer, command = lambda: self.Account(self.accountFrame), 
                                          width = 50, bg = Constants.navBarColor, highlightthickness = 0, 
                                          activeforeground = Constants.navBarColor, activebackground = Constants.navBarColor, image = self.accountIcon)

        self.investmentNavButton = Button(master = self.navButtonContainer, command = lambda: self.Investment(self.investmentFrame), 
                                          width = 50, bg = Constants.navBarColor, highlightthickness = 0, 
                                          activeforeground = Constants.navBarColor, activebackground = Constants.navBarColor, image = self.investmentIcon)


        self.mainMenuNavButton.grid  (row = 0, column = 0)
        self.plannerNavButton.grid   (row = 1, column = 0)
        self.accountNavButton.grid   (row = 2, column = 0)
        self.investmentNavButton.grid(row = 3, column = 0)
    
    def ShowNavBar(self):
        global navBarIsShown
        if ("navBarIsShown" in globals()):
            if (not navBarIsShown):
                self.navBarFrame.place(relx = 0, rely = 0, anchor = "nw")
                navBarIsShown = True
        else:
            self.navBarFrame.place(relx = 0, rely = 0, anchor = "nw")
            navBarIsShown = True

    def HideNavBar(self):
        global navBarIsShown
        if ("navBarIsShown" in globals()):
            if (navBarIsShown):
                self.navBarFrame.place(relx = 0, rely = 0, anchor = "se")
                navBarIsShown = False
        else:
            self.navBarFrame.place(relx = 0, rely = 0, anchor = "se")
            navBarIsShown = False

        pass


# Sub window Changer

    def MainMenu(self, parent: Frame):
        self.HideLastWindow()
        self.mainMenuFrame.pack(fill = "both", expand = 1)
        self.HideNavBar()

        self.currentSubWindow = Constants.mainMenuSub

    def Planner(self, parent: Frame):
        self.HideLastWindow()
        parent.pack(fill = "both", expand = 1)
        self.ShowNavBar()

        self.currentSubWindow = Constants.plannerSub
        pass

    def Account(self, parent: Frame):
        self.HideLastWindow()
        parent.pack(fill = "both", expand = 1)
        self.ShowNavBar()

        self.currentSubWindow = Constants.accountSub
        pass

    def Investment(self, parent: Frame):
        self.HideLastWindow()
        parent.pack(fill = "both", expand = 1)
        self.ShowNavBar()

        self.currentSubWindow = Constants.investmentSub
        pass


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
