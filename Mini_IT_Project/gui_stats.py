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
from collections import Counter
import datetime
import calendar
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

        main.SaveAll()

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
        self.root.geometry("1400x800")
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

        allTransactions = []

        if (self.accounts is None):
            return

        for i in self.accounts:
            for j in i.transactions:
                allTransactions.append(j)

        allTransDates = []
        for i in allTransactions:
            allTransDates.append(i.creationDateTime.date())

        countDates = dict()
        for i in allTransDates:
            countDates[i] = countDates.get(i, 0) + 1

        dates = []
        for i in countDates.keys():
            dates.append(i.strftime("%d-%m-%Y"))
        values = list(countDates.values())

        fig, axs = plt.subplots()
        axs.plot(dates, values)
        fig.suptitle('User Activity')

        #plt.show()


        canvas = FigureCanvasTkAgg(fig, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 2)



        label = Label(self.viewingFrame, text = "Income", font = ("", 36), bg = Constants.mainWindowBgColor)
        label.grid(row = 1, column = 0)

        label = Label(self.viewingFrame, text = "Spending", font = ("", 36), bg = Constants.mainWindowBgColor)
        label.grid(row =1 , column = 1)



        parentCats = []
        for i in self.guiAcc.categories:
            parentCats.append(i.GetRootParent())
        parentCats = list(dict.fromkeys(parentCats))

        for i in range(len(parentCats)):
            parentCats[i] = parentCats[i].name

        rootIncome = dict()
        rootSpending = dict()

        for i in parentCats:
            rootIncome[i] = 0
            rootSpending[i] = 0

        for i in allTransactions:
            if (i.category != None):
                rootCat = i.category.GetRootParent().name
                amount = i.amount
                if (not i.isIncome):
                    rootSpending[rootCat] += amount
                else:
                    rootIncome[rootCat] += amount

        max = 0
        index = 0
        targetIndex = -1
        rootIncomeX = rootIncome.copy()
        for instance in rootIncome:
            key = instance
            value = rootIncome[key]
            if value == 0:
                del rootIncomeX[key]
        rootIncome = rootIncomeX
        for i in rootIncome:
            value = rootIncome[i]
            if value > max:
                max = value
                targetIndex = index
            index += 1

        explode = []
        for i in range(len(rootIncome)):
            explode.append(0)

        if (targetIndex != -1):
            explode[targetIndex] = 0.1

        labels = [i for i in rootIncome]
        data = [rootIncome[i] for i in rootIncome]

        fig1, ax1 = plt.subplots()
        ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 2, column = 0)


        max = 0
        index = 0
        targetIndex = -1
        rootSpendingX = rootSpending.copy()
        for instance in rootSpending:
            key = instance
            value = rootSpending[key]
            if value == 0:
                del rootSpendingX[key]
        rootSpending = rootSpendingX
        for i in rootSpending:
            value = rootSpending[i]
            if value > max:
                max = value
                targetIndex = index
            index += 1

        explode = []
        for i in range(len(rootSpending)):
            explode.append(0)
        
        if (targetIndex != -1):
            explode[targetIndex] = 0.1

        labels = [i for i in rootSpending]
        data = [rootSpending[i] for i in rootSpending]

        fig1, ax1 = plt.subplots()
        ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 2, column = 1)


        incomes = dict()
        spendings = dict()

        for i in self.guiAcc.categories:
            incomes[i.name] = 0
            spendings[i.name] = 0

        for i in allTransactions:
            if (i.category != None):
                if (i.isIncome):
                    incomes[i.category.name] += i.amount
                else:
                    spendings[i.category.name] += i.amount

        max = 0
        index = 0
        targetIndex = -1
        incomesX = incomes.copy()
        for instance in incomes:
            key = instance
            value = incomes[key]
            if value == 0:
                del incomesX[key]
        incomes = incomesX
        for i in incomes:
            value = incomes[i]
            if value > max:
                max = value
                targetIndex = index
            index += 1

        explode = []
        for i in range(len(incomes)):
            explode.append(0)

        if (targetIndex != -1):
            explode[targetIndex] = 0.1

        labels = [i for i in incomes]
        data = [incomes[i] for i in incomes]

        fig1, ax1 = plt.subplots()
        ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 3, column = 0)



        max = 0
        index = 0
        targetIndex = -1
        spendingsX = spendings.copy()
        for instance in spendings:
            key = instance
            value = spendings[key]
            if value == 0:
                del spendingsX[key]
        spendings = spendingsX
        for i in spendings:
            value = spendings[i]
            if value > max:
                max = value
                targetIndex = index
            index += 1

        explode = []
        for i in range(len(spendings)):
            explode.append(0)

        if (targetIndex != -1):
            explode[targetIndex] = 0.1

        labels = [i for i in spendings]
        data = [spendings[i] for i in spendings]

        fig1, ax1 = plt.subplots()
        ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 3, column = 1)

        years = []
        for i in allTransactions:
            years.append(i.date.year)
        years = list(dict.fromkeys(years))

        yearlyFrame = Frame(self.viewingFrame)
        yearlyFrame.grid(row = 4, column = 0, columnspan = 2)
        index = 0
        for i in years:

            incomeMonths = dict()
            for j in range(1, 13):
                incomeMonths[j] = 0
            #Income
            for j in incomeMonths:
                for k in allTransactions:
                    if (k.isIncome and i == k.date.year and j == k.date.month):
                        incomeMonths[j] += k.amount

            incomeMonthsX = incomeMonths.copy()
            for j in incomeMonths:
                if (incomeMonths[j] == 0):
                    del incomeMonthsX[j]
            incomeMonths = incomeMonthsX
            incomeMonthsX = dict()
            for j in incomeMonths:
                incomeMonthsX[calendar.month_name[j]] = incomeMonths[j]
            incomeMonths = incomeMonthsX

            fig, axs = plt.subplots()
            axs.plot(list(incomeMonths.keys()), list(incomeMonths.values()))
            fig.suptitle(i)

            canvas = FigureCanvasTkAgg(fig, yearlyFrame)
            canvas.draw()
            canvas.get_tk_widget().grid(row = index, column = 0)

            #Spending
            spendingMonths = dict()
            for j in range(1, 13):
                spendingMonths[j] = 0
            for j in spendingMonths:
                for k in allTransactions:
                    if (not k.isIncome and i == k.date.year and j == k.date.month):
                        spendingMonths[j] += k.amount        

            spendingMonthsX = spendingMonths.copy()
            for j in spendingMonths:
                if (spendingMonths[j] == 0):
                    del spendingMonthsX[j]
            spendingMonths = spendingMonthsX
            spendingMonthsX = dict()
            for j in spendingMonths:
                spendingMonthsX[calendar.month_name[j]] = spendingMonths[j]
            spendingMonths = spendingMonthsX

            fig, axs = plt.subplots()
            axs.plot(list(spendingMonths.keys()), list(spendingMonths.values()))
            fig.suptitle(i)

            canvas = FigureCanvasTkAgg(fig, yearlyFrame)
            canvas.draw()
            canvas.get_tk_widget().grid(row = index, column = 1)


            index += 1





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
        #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        #sizes = [15, 30, 45, 10]
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        #fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        #        shadow=True, startangle=90)
        #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


        #canvas = FigureCanvasTkAgg(fig1, self.viewingFrame)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row = 3, column = 0)

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
