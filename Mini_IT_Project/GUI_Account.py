# Raven
from tkinter import Frame, ttk, Entry, Button, StringVar, OptionMenu, Label, BOTH, Canvas
from tkcalendar import Calendar
import Constants
import Interfaces
import Account
import GUI_Stats
import datetime

class GUI_Account(Interfaces.IOnSave):

    accounts = []
    categories = []

    def OnSave(self):
        self.Main.SaveData("AccountsList", self.accounts)
        self.Main.SaveData("CategoriesList", self.categories)
        self.Main.SaveData("SelectedAccount", self.selectedAccount)

    def GoToStatistics(self, parent:Frame):
        GUI_Stats.Statistics(parent)

    def __init__(self, parent: Frame, main):

        self.Main = main
        self.parent = parent
        super().__init__(main)
        self.accounts = main.GetSavedData("AccountsList")
        self.categories = main.GetSavedData("CategoriesList")
        self.selectedAccount = main.GetSavedData("SelectedAccount")
    
        if (self.accounts is None):
            self.NewUserAccounts()
        else:
            self.LoadAccounts()
        if (self.categories is None):
            self.NewUserCategories()
        else:
            self.LoadCategories()
        if (self.selectedAccount is None):
            self.selectedAccount = self.accounts[0]

        self.InitTransHistory()
        self.InitAccountFrame()
        self.InitIncomeExpenseFrame()
        self.RefreshAccountSelect()
        
        self.statsButton = Button(master = parent, text= "Statistics", command = lambda : self.GoToStatistics(parent)) 
        self.statsButton.place(x = 60, y = 710, anchor = "sw")




    def InitIncomeExpenseFrame(self):

        self.transactionAdderFrame = Frame(master = self.parent, width = 300, height = 680, bg = Constants.mainWindowAltColor)
        self.transactionAdderFrame.pack_propagate(0)
        self.transactionAdderFrame.place(relx = 0.99, rely = 0.5, anchor = "e")

        def AmountVerifier(currentString):
            try:
                dotCount = 0
                for i in currentString.get():
                    if (i != "."):
                        int(i)
                    else:
                        dotCount += 1
                if (dotCount > 1):
                    int("a")    # Shameful Haha
                self.previousAmount = currentString.get()
            except ValueError:
                currentString.set(self.previousAmount)

        self.previousAmount     = ""
        self.enteredAmount      = StringVar()
        self.enteredAmount.trace("w", lambda name, index, mode, currentString = self.enteredAmount: AmountVerifier(currentString))
        self.LAmount            = Label(master = self.transactionAdderFrame, text = "Amount:", bg = Constants.mainWindowAltColor)
        self.transAmountEntry   = Entry(master = self.transactionAdderFrame, textvariable = self.enteredAmount)

        self.enteredTitle   = StringVar()
        self.LTitle         = Label(master = self.transactionAdderFrame, text = "Title:", bg = Constants.mainWindowAltColor)
        self.transTitle     = Entry(master = self.transactionAdderFrame, textvariable = self.enteredTitle)

        self.enteredOtherSubject    = StringVar()
        self.LOtherSubject          = Label(master = self.transactionAdderFrame, text = "Transfer Subject \n[Enter Account Name to link]:", bg = Constants.mainWindowAltColor)
        self.transOtherSubject      = Entry(master = self.transactionAdderFrame, textvariable = self.enteredOtherSubject)

        self.enteredDesc    = StringVar()
        self.LDesc          = Label(master = self.transactionAdderFrame, text = "Note:", bg = Constants.mainWindowAltColor)
        self.transDesc      = Entry(master = self.transactionAdderFrame, textvariable = self.enteredDesc)

        def ClearTransDetails():
            self.previousAmount = ""
            self.enteredAmount.set("")
            self.enteredOtherSubject.set("")
            self.enteredTitle.set("")
            self.enteredDesc.set("")
            self.transCalendar.selection_set(datetime.date.today())

        def AddTransaction(isIncome):
            self.AddTransaction(isIncome)
            ClearTransDetails()
            self.RefreshAccountBalance()

        self.transIncomeButton  = Button(master = self.transactionAdderFrame, text = "Add as Income",  command = lambda: AddTransaction(True), bg = Constants.mainWindowAltColor)
        self.transExpenseButton = Button(master = self.transactionAdderFrame, text = "Add as Expense", command = lambda: AddTransaction(False), bg = Constants.mainWindowAltColor)
        self.transCancelButton  = Button(master = self.transactionAdderFrame, text = "Clear", command = ClearTransDetails, bg = Constants.mainWindowAltColor)


        #Calendar
        self.LCalendar     = Label(master = self.transactionAdderFrame, text = "Date:", bg = Constants.mainWindowAltColor)
        self.transCalendar = Calendar(self.transactionAdderFrame, 
                                      font = "Arial 8", selectmode = 'day', cursor = "hand1", 
                                      year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)


        ## BELOW ## Category Section
    
        self.LCategory     = Label(master = self.transactionAdderFrame, text = "Category:", bg = Constants.mainWindowAltColor)
        self.categoryFrame = Frame(master = self.transactionAdderFrame, width = 300, height = 250)
        #self.categoryFrame.place(relx = 0.5, rely = 0.99, anchor = "s")

        self.displayCategoryTree = ttk.Treeview(self.categoryFrame)
        self.GrowCategoryTree(self.displayCategoryTree)
        self.displayCategoryTree.grid(row = 0, column = 0, columnspan = 2)
        #self.displayCategoryTree.place(relx = 0.5, rely = 0, anchor = "n")
        self.displayCategoryTree.column("#0", width = 280)

        def updateScroll(event):
            self.displayCategoryTree.configure(yscrollcommand = self.categorySBY.set)
            self.displayCategoryTree.configure(xscrollcommand = self.categorySBX.set)
            
        self.categorySBY = ttk.Scrollbar(master = self.categoryFrame, orient = "vertical", command = self.displayCategoryTree.yview)
        self.categorySBX = ttk.Scrollbar(master = self.categoryFrame, orient = "horizontal", command = self.displayCategoryTree.xview)

        self.categorySBY.grid(row = 0, column = 2, sticky = "nse")
        self.categorySBX.grid(row = 1, column = 0, columnspan = 2, sticky = "wes")
        
        self.displayCategoryTree.bind("<Configure>", updateScroll)

        def OnCategoryEntryChanged(entryText):
            state = self.CheckCategory(entryText.get())
            if (state == 0):
                self.addCategoryEntry.configure(fg = "red")
                self.addCategoryButton.grid_forget()
            elif (state == 1):
                self.addCategoryEntry.configure(fg = "red")
                self.addCategoryButton.grid_forget()
            else:
                self.addCategoryEntry.configure(fg = "black")
                self.addCategoryButton.grid(row = 2, column = 2)

        def ButtonCreateCategory(): 
            if (self.CheckCreateCategory(self.addCategoryEntry.get(), self.displayCategoryTree.item(self.displayCategoryTree.focus())["text"])):
                self.RefreshCategory()
            else:
                print("Error Creating Category")
            self.entryStrVar.set("")

        self.entryStrVar = StringVar()
        self.entryStrVar.trace("w", lambda name, index, mode, sv=self.entryStrVar: OnCategoryEntryChanged(sv))

        self.addCategoryEntry = Entry(master = self.categoryFrame, textvariable = self.entryStrVar, width = 30)
        self.addCategoryEntry.grid(row = 2, column = 0, columnspan = 2)
        self.addCategoryEntry.bind("<Return>", lambda e: ButtonCreateCategory())

        self.addCategoryButton = Button(master = self.categoryFrame, text = "+", command = ButtonCreateCategory)

        self.LAmount.grid           (row = 0, column = 0)
        self.transAmountEntry.grid  (row = 0, column = 1, padx = (0, 2))
        self.LTitle.grid            (row = 1, column = 0)
        self.transTitle.grid        (row = 1, column = 1, padx = (0, 2))
        self.LOtherSubject.grid     (row = 2, column = 0)
        self.transOtherSubject.grid (row = 2, column = 1, padx = (0, 2))
        self.LDesc.grid             (row = 3, column = 0)
        self.transDesc.grid         (row = 3, column = 1, padx = (0, 2))
        
        self.LCalendar.grid             (row = 4, column = 0, padx = (0, 100))
        self.transCalendar.grid         (row = 5, column = 0, columnspan = 2, pady = (3, 3), padx = (5, 5))
        self.LCategory.grid             (row = 6, column = 0, padx = (0, 100))
        self.categoryFrame.grid         (row = 7, column = 0, columnspan = 2, pady = (0, 3), padx = (5, 5))
        self.transCancelButton.grid     (row = 8, column = 1, rowspan = 2,    pady = (0, 2))
        self.transIncomeButton.grid     (row = 8, column = 0, columnspan = 1, pady = (0, 2))
        self.transExpenseButton.grid    (row = 9, column = 0, columnspan = 1, pady = (0, 2))
        
    def InitAccountFrame(self):

        self.accountChoiceFrame = Frame(master = self.parent, bg = Constants.mainWindowBgColor)
        self.accountChoiceFrame.place(x = 60, y = 60, anchor = "nw")

        self.accountChoice = StringVar()
        def AccountChoiceChanged(choice):
            for i in self.accounts:
                if (choice == i.name):
                    self.AccountSelect(i)
                    break
        
        self.accountChoice.trace("w", lambda name, index, mode, choice = self.accountChoice: AccountChoiceChanged(choice.get()))

        self.LAccountChoice = Label(self.accountChoiceFrame, text = "Operating Account:", font = "Arial 8", bg = Constants.mainWindowBgColor)
        self.LAccountChoice.grid(row = 0, column = 0, columnspan = 2)

        accountNames = [i.name for i in self.accounts]

        self.accountChoiceDropdown = OptionMenu(self.accountChoiceFrame, self.accountChoice, *accountNames)


        self.balanceDisplay = Label(master = self.accountChoiceFrame, font = "Arial 14", bg = Constants.mainWindowBgColor)
        self.balanceDisplay.grid(row = 1, column = 1)
        


        ## Add Account Below ##
        self.addAccFrame = Frame(master = self.accountChoiceFrame, bg = Constants.mainWindowAltColor)
        self.addAccFrame.grid(row = 0, column = 3, rowspan = 2, padx = (10, 10))

        def AddAccount(isBank):
            name = self.addAccEntrySV.get()
            if (isBank):
                acc = Account.BankAccount()
            else:
                acc = Account.Account()
            acc.name = name
            self.accounts.append(acc)
            self.addAccEntrySV.set("")
            self.selectedAccount = acc
            self.RefreshAccountSelect()

        self.addAccEntrySV = StringVar()
        self.addAccEntry = Entry(master = self.addAccFrame, textvariable = self.addAccEntrySV, width = 35)
        self.addAccButton = Button(master = self.addAccFrame, text = "Add Normal Account", command = lambda: AddAccount(False))
        self.addAccButton2 = Button(master = self.addAccFrame, text = "Add Bank Account", command = lambda: AddAccount(True))

        self.addAccEntry.grid(row = 0, column = 0, columnspan = 2, pady = (1, 1))
        self.addAccButton.grid(row = 1, column = 0, padx = (1, 1))
        self.addAccButton2.grid(row = 1, column = 1, padx = (1, 1))



        ## INTERESTS BELOW ##

        self.interestFrame = Frame(master = self.accountChoiceFrame, bg = Constants.mainWindowAltColor)

        self.LInterestTxt = Label(master = self.interestFrame, text = "Interests:")
        self.LInterest = Label(master = self.interestFrame)    # Label is for text, we'll use later for displaying

        self.interestEntrySV = StringVar()  # this is to catch input from entry
        self.accountInterestEntry = Entry(master = self.interestFrame, textvariable = self.interestEntrySV, width = 6) #This is Entry, for the user to put in their desired interest
        self.accountInterestButton = Button (master = self.interestFrame, text = "Update Interest")  # After the user sets the interest in the Entry, the user will press this button to SET

        self.LInterestTxt.grid          (row = 0, column = 0)
        self.LInterest.grid             (row = 0, column = 1)
        self.accountInterestEntry.grid  (row = 1, column = 0)
        self.accountInterestButton.grid (row = 1, column = 1)

        # This is my custom value checker, quite powerful haha
        def AmountVerifier(currentString):
            try:
                dotCount = 0
                for i in currentString.get():
                    if (i != "."):
                        int(i)
                    else:
                        dotCount += 1
                if (dotCount > 1):
                    int("a")    # Shameful Haha
                self.previousInterest = currentString.get()
            except ValueError:
                currentString.set(self.previousInterest)

        def SetInterest():
            self.selectedAccount.SetInterests(float(self.interestEntrySV.get()))
            self.LInterest.configure(text = str(self.selectedAccount.interestRate) + "%")

        
        self.previousInterest = ""
        self.interestEntrySV.trace("w", lambda name, index, mode, sv = self.interestEntrySV: AmountVerifier(sv))    #This verifies the number thing

        self.accountInterestButton.configure(command = SetInterest)     #Here we set the interest

        # Test Button #

        def GETRICH():
            self.selectedAccount.GainInterests()
            self.RefreshTransHistory()
            self.RefreshAccountBalance()

        self.GetRichButton = Button(master = self.parent, text = "Get Rich By Interests", command = GETRICH)
        self.GetRichButton.place(relx = 0.5, rely = 0.99, anchor = "s")
    

        self.AccountSelect(self.selectedAccount)
    
    def InitTransHistory(self):
        
        def updateScroll(event):
            self.transHistoryTree.configure(yscrollcommand = self.transHistorySBY.set)
            self.transHistoryTree.configure(xscrollcommand = self.transHistorySBX.set)
            

        self.transHistoryFrame = Frame(master = self.parent, bg = Constants.mainWindowBgColor)
        self.transHistoryTree = ttk.Treeview(master = self.transHistoryFrame, height = 24)
        self.transHistorySBY = ttk.Scrollbar(master = self.transHistoryFrame, orient = "vertical", command = self.transHistoryTree.yview)
        self.transHistorySBY.grid(row = 0, column = 1, sticky = "nse")
        self.transHistorySBX = ttk.Scrollbar(master = self.transHistoryFrame, orient = "horizontal", command = self.transHistoryTree.xview)
        self.transHistorySBX.grid(row = 1, column = 0, sticky = "wes")
        self.transHistoryTree.bind("<Configure>", updateScroll)


    def RefreshAccountSelect(self):
        self.accountChoiceDropdown.grid_forget()
        accountNames = [i.name for i in self.accounts]
        self.accountChoiceDropdown = OptionMenu(self.accountChoiceFrame, self.accountChoice, *accountNames)
        self.accountChoiceDropdown["font"] = "Arial 14"
        self.accountChoiceDropdown["bg"] = Constants.mainWindowBgColor
        self.accountChoiceDropdown.grid(row = 1, column = 0)
        self.AccountSelect(self.selectedAccount)

    def AddTransaction(self, isIncome):
        conversion = 0
        try:
            conversion = float(self.enteredAmount.get())
        except ValueError:
            conversion = None
            print("Conversion Error!!, Entered amount ain't a float")
        trans = Account.Transaction()
        trans.amount = conversion

        targetOtherSubject = self.enteredOtherSubject.get()
        for i in self.accounts:
            if (i.name == targetOtherSubject):
                targetOtherSubject = i  # Target Account

                transOther          = Account.Transaction()
                transOther.amount       = conversion
                transOther.isIncome     = not isIncome          # DIFFERENCE
                transOther.otherSubject = self.selectedAccount  # DIFFERENCE
                transOther.title        = self.enteredTitle.get()
                transOther.description  = self.enteredDesc.get()
                transOther.date         = self.transCalendar.selection_get()
                transOther.category     = self.GetCategoryByName(self.displayCategoryTree.item(self.displayCategoryTree.focus())["text"])
                
                targetOtherSubject.AddTransaction(transOther)

                break
        
        trans.isIncome      = isIncome
        trans.otherSubject  = targetOtherSubject
        trans.title         = self.enteredTitle.get()
        trans.description   = self.enteredDesc.get()
        trans.date          = self.transCalendar.selection_get()
        trans.category      = self.GetCategoryByName(self.displayCategoryTree.item(self.displayCategoryTree.focus())["text"])
        self.selectedAccount.AddTransaction(trans)
        self.RefreshTransHistory()

    def RefreshTransHistory(self):

        transactions = self.selectedAccount.transactions

        try:
            self.transHistoryFrame.place_forget()
        except Exception:
            pass
        self.transHistoryTree.delete(*self.transHistoryTree.get_children())

        self.transHistoryFrame.place(x = 60, y = 140, anchor = "nw")
        self.transHistoryTree.grid(row = 0, column = 0)
        #self.transHistoryFrame.grid_rowconfigure(0, minsize = 400)

        self.transHistoryTree["columns"] = ("Title", "Amount", "Subject", "Category", "Description", "Date", "Time Created")

        self.transHistoryTree.column("#0", width = 40)
        self.transHistoryTree.column("#1", width = 100)
        self.transHistoryTree.column("#2", width = 75)
        self.transHistoryTree.column("#3", width = 100)
        self.transHistoryTree.column("#4", width = 100)
        self.transHistoryTree.column("#5", width = 100)
        self.transHistoryTree.column("#6", width = 75)
        self.transHistoryTree.column("#7", width = 120)

        self.transHistoryTree.heading("#1", text = "Title")
        self.transHistoryTree.heading("#2", text = "Amount")
        self.transHistoryTree.heading("#3", text = "Subject")
        self.transHistoryTree.heading("#4", text = "Category")
        self.transHistoryTree.heading("#5", text = "Description")
        self.transHistoryTree.heading("#6", text = "Date")
        self.transHistoryTree.heading("#7", text = "Time Created")

        for i in range(0, len(transactions)):
            self.GrowTransactionHistory(self.transHistoryTree, transactions[i], i)

        pass

    def GrowTransactionHistory(self, tree: ttk.Treeview, transaction: Account.Transaction, index):
        
        subject = transaction.otherSubject
        category = transaction.category
        if (category is not None):
            category = transaction.category.GetFullPath()
        if (type(transaction.otherSubject) is Account.Account):
            subject = transaction.otherSubject.name
        amount = transaction.amount
        if (not transaction.isIncome):
            amount = "-" + str(amount)
        
        tree.insert("", index, text = str(index + 1), values = (transaction.title, amount, subject, category, transaction.description, transaction.date, transaction.creationDateTime.strftime("%m/%d/%Y, %H:%M:%S")))
        
        pass

    def AccountSelect(self, selectedAccount):

        if (selectedAccount is None):
            return

        self.balanceDisplay.configure(text = selectedAccount.GetBalance())  # This is where we update the amount

        if isinstance(selectedAccount, Account.BankAccount):   # Here we check the type, if it's like Cash In Hand Account we WONT disply the text
            self.interestFrame.grid(row = 0, column = 4, rowspan = 2, padx = (40, 0))   #This should work, i also not sure for Python, that's why we test
            self.LInterest.configure(text = str(selectedAccount.interestRate) + "%")

        else:
            self.interestFrame.grid_forget()

        self.selectedAccount = selectedAccount
        self.accountChoice.set(selectedAccount.name)
        self.RefreshTransHistory()
        
    def RefreshAccountBalance(self):
        self.balanceDisplay.configure(text = self.selectedAccount.GetBalance())

    def NewUserCategories(self):
        self.categories = []
        self.categoryShopping = Account.Category("Shopping")
        self.categories.append(self.categoryShopping)
        self.categories.append(Account.Category("Other"))
        self.categories.append(Account.Category("Clothing", self.categoryShopping))

    def LoadCategories(self):
        pass

    def RefreshCategory(self):
        self.displayCategoryTree.delete(*self.displayCategoryTree.get_children())
        self.GrowCategoryTree(self.displayCategoryTree)

    def GrowCategoryTree(self, tree):
        tree.heading("#0", text = "Categories")

        def NestCategory(category, parent):
            tree.insert(parent.name, "end", category.name, text = category.name)
        def BaseCategory(category):
            tree.insert("", "end", category.name, text = category.name)
        for i in self.categories:
            if (i.parent is None):
                BaseCategory(i)
            else:
                NestCategory(i, i.parent)

    def LoadAccounts(self):
        pass

    def NewUserAccounts(self):
        self.accounts = []
        cashAccount = Account.Account()
        cashAccount.name = "Cash In Hand"
        bankAccount = Account.BankAccount()
        bankAccount.name = "Bank Account"

        self.accounts.append(cashAccount)
        self.accounts.append(bankAccount)

    def CheckCategory(self, name):
        if (name == "" or name is None):
            return 0
        for i in self.categories:
            if (i.name == name):
                return 1
        return 2

    def CheckCreateCategory(self, name, parentName):
        state = self.CheckCategory(name)
        if (state == 0 or state == 1):
            return False
        if (parentName is ""):
            parentName = None
        self.categories.append(Account.Category(name, self.GetCategoryByName(parentName)))
        return True

    def GetCategoryByName(self, parentName):
        for i in self.categories:
            if (i.name == parentName):
                return i
        return None
