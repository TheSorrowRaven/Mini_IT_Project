###
#/***************************************************
#File Name: gui_stats.py
#Version/Date: 0.4 (2020-05-13)
#Programmer/ID: Raja Muhammad Darwisy bin Raja Ahmad(11911000792), Fong Zheng Wei(1191100350)
#Project Name: Smart Finance Manager 
#Teammates: Raven Lim Zhe Xuan , Nagaindran A/L Kanaseelanayagam, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

from tkinter import Frame, Tk, Label, ttk, Canvas
import gui_account as GUI_Account
import account as Account
import interfaces as Interfaces
import constants as Constants
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Statistics():

    """ 
    self.guiAcc
    self.thisAccount
    self.allAccounts 

    self.allTransactions
    self.thisTransactions

    self.totalBalance
    self.thisBalance
    """

    def __init__(self, guiAcc, main):

        self.guiAcc = guiAcc
        self.thisAccount = guiAcc.selectedAccount
        self.allAccounts = guiAcc.accounts

        self.accounts = main.GetSavedData("AccountsList")
        self.categories = main.GetSavedData("CategoriesList")
        self.selectedAccount = main.GetSavedData("SelectedAccount")

        self.InitData()
        self.Main = main



        self.root = Tk()
        self.root.title("Account Statistics")
        self.root.geometry("800x800")
        self.root.resizable(False, False)


        self.parent = Canvas(self.root, borderwidth = 0, highlightthickness = 0, bg = Constants.mainWindowBgColor)
        self.viewingFrame = Frame(self.parent, bg = Constants.mainWindowBgColor)
        self.parentSB = ttk.Scrollbar(self.root, orient = "vertical", command = self.parent.yview)
        self.parent.configure(yscrollcommand = self.parentSB.set)

        self.parentSB.pack(side = "right", fill = "y")
        self.parent.pack(side = "left", fill = "both", expand = True)
        self.parent.create_window((4, 4), window = self.viewingFrame, anchor = "nw")

        self.viewingFrame.bind("<Configure>", lambda event, canvas = self.parent: canvas.configure(scrollregion = canvas.bbox("all")))

        self.InitWindow()



        self.root.mainloop()

    def InitData(self):
        self.allTransactions = []
        for i in self.allAccounts:
            for j in i.transactions:
                self.allTransactions.append(j)

        self.thisTransactions = []
        for i in self.thisAccount.transactions:
            self.thisTransactions.append(i)

        self.totalBalance = 0
        for i in self.allAccounts:
            self.totalBalance += i.GetBalance()

        self.thisBalance = self.thisAccount.GetBalance()

    def InitWindow(self):
        
        self.LTitle = Label(master = self.viewingFrame, text = "STATISTICS", font = ("", 18), bg = Constants.mainWindowBgColor)
        self.LTitle.grid(row = 0, column = 0, columnspan = 2)







        #Example 1
        # Fixing random state for reproducibility
        #np.random.seed(19680801)

        # Compute areas and colors
        #N = 150
        #r = 2 * np.random.rand(N)
        #theta = 2 * np.pi * np.random.rand(N)
        #area = 200 * r**2
        #colors = theta

        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection = 'polar')
        #c = ax.scatter(theta, r, c = colors, s = area, cmap = 'hsv', alpha = 0.75)

        #canvas = FigureCanvasTkAgg(fig, self.viewingFrame)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row = 1, column = 0)
        

        #Example 2
        #f = Figure(figsize=(5,5), dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])


        #canvas = FigureCanvasTkAgg(f, self.viewingFrame)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row = 2, column = 0)



        #Example 3
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


        canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 3, column = 0)


        # #transactionsSortedTemp = [None] * len(transactions)
        # for _ in range(len(transactions)):
        #     for i in range(len(transactions) - 1):
        #         tempTransaction = transactions[i]
        #         tempTransaction2 = transactions[i+1]
        #         if (tempTransaction.creationDateTime < tempTransaction2.creationDateTime):
        #             transactions[i] = tempTransaction
        #             transactions[i+1] = tempTransaction2
        #         else:
        #             transactions[i] = tempTransaction2
        #             transactions[i+1] = tempTransaction




        
    
if __name__ == "__main__":
    print("Please run main.py instead")
    pass
