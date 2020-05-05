# Raven
from tkinter import Frame, ttk, Entry, Button, StringVar, OptionMenu, Label
import Constants
import Interfaces
import Account

class GUI_Account(Interfaces.IOnSave):

    accounts = []
    categories = []

    def OnSave(self):
        self.Main.SaveData("AccountsList", self.accounts)
        self.Main.SaveData("CategoriesList", self.categories)
        self.Main.SaveData("SelectedAccount", self.selectedAccount)

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

        self.categoryFrame = Frame(master = parent, width = 400, height = 300)
        self.categoryFrame.place(relx = 0.5, rely = 0.5, anchor = "nw")


        self.displayCategoryTree = ttk.Treeview(self.categoryFrame)
        self.GrowCategoryTree(self.displayCategoryTree)
        self.displayCategoryTree.place(relx = 0.5, rely = 0, anchor = "n")
        self.displayCategoryTree.column("#0", width = 380)

        def OnCategoryEntryChanged(entryText):
            state = self.CheckCategory(entryText.get())
            if (state == 0):
                self.addCategoryEntry.configure(fg = "red")
                self.addCategoryButton.place(relx = 1, rely = 1, anchor = "nw")
                # Hide add button
            elif (state == 1):
                self.addCategoryEntry.configure(fg = "red")
                self.addCategoryButton.place(relx = 1, rely = 1, anchor = "nw")
                # Hide add button and color text red
            else:
                self.addCategoryEntry.configure(fg = "black")
                self.addCategoryButton.place(relx = 0.9, rely = 0.9, anchor = "se")
                # Show add button

        self.entryStrVar = StringVar()
        self.entryStrVar.trace("w", lambda name, index, mode, sv=self.entryStrVar: OnCategoryEntryChanged(sv))

        def ButtonCreateCategory(): 
            if (self.CheckCreateCategory(self.addCategoryEntry.get(), self.displayCategoryTree.item(self.displayCategoryTree.focus())["text"])):
                self.RefreshCategory()
            else:
                print("Error Creating Category")

        self.addCategoryEntry = Entry(master = self.categoryFrame, textvariable = self.entryStrVar, width = 30)
        self.addCategoryEntry.place(relx = 0.1, rely = 0.9, anchor = "sw")
        self.addCategoryEntry.bind("<Return>", lambda e: ButtonCreateCategory())

        self.addCategoryButton = Button(master = self.categoryFrame, text = "+", command = ButtonCreateCategory)
        


        self.accountChoiceFrame = Frame(master = parent)
        self.accountChoiceFrame.pack()

        accountNames = [i.name for i in self.accounts]

        self.accountChoice = StringVar()
        def AccountChoiceChanged(choice):
            for i in self.accounts:
                if (choice == i.name):
                    self.AccountSelect(i)
                    break
        
        self.accountChoice.trace("w", lambda name, index, mode, choice = self.accountChoice: AccountChoiceChanged(choice.get()))

        self.accountChoiceDropdown = OptionMenu(self.accountChoiceFrame, self.accountChoice, *accountNames)
        self.accountChoiceDropdown.pack()

        self.balanceDisplay = Label(master = self.accountChoiceFrame)
        self.balanceDisplay.pack()

        self.AccountSelect(self.selectedAccount)

        self.transactionAdderFrame = Frame(master = parent)
        self.transactionAdderFrame.pack()

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

        self.previousAmount = ""
        self.enteredAmount = StringVar()
        self.enteredAmount.trace("w", lambda name, index, mode, currentString = self.enteredAmount: AmountVerifier(currentString))
        self.LAmount = Label(master = self.transactionAdderFrame, text = "Amount:")
        self.transAmountEntry = Entry(master = self.transactionAdderFrame, textvariable = self.enteredAmount)

        self.enteredTitle = StringVar()
        self.LTitle = Label(master = self.transactionAdderFrame, text = "Title:")
        self.transTitle = Entry(master = self.transactionAdderFrame, textvariable = self.enteredTitle)

        self.enteredOtherSubject = StringVar()
        self.LOtherSubject = Label(master = self.transactionAdderFrame, text = "Transfer Subject (optional) \n[Enter Account Name to transfer to another account]:")
        self.transOtherSubject = Entry(master = self.transactionAdderFrame, textvariable = self.enteredOtherSubject)

        self.enteredDesc = StringVar()
        self.LDesc = Label(master = self.transactionAdderFrame, text = "Note (optional):")
        self.transDesc = Entry(master = self.transactionAdderFrame, textvariable = self.enteredDesc)

        def ClearTransDetails():
            self.previousAmount = ""
            self.enteredAmount.set("")
            self.enteredOtherSubject.set("")
            self.enteredTitle.set("")
            self.enteredDesc.set("")

        def AddTransaction():
            self.AddTransaction()
            ClearTransDetails()

        self.transDoneButton = Button(master = self.transactionAdderFrame, text = "Done/Add", command = AddTransaction)
        self.transCancelButton = Button(master = self.transactionAdderFrame, text = "Clear", command = ClearTransDetails)

        self.LAmount.pack()
        self.transAmountEntry.pack()
        self.LTitle.pack()
        self.transTitle.pack()
        self.LOtherSubject.pack()
        self.transOtherSubject.pack()
        self.LDesc.pack()
        self.transDesc.pack()

        self.transDoneButton.pack()
        self.transTitle.pack()
        self.transOtherSubject.pack()


    def AddTransaction(self):
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
                targetOtherSubject = i
                break

        trans.otherSubject = targetOtherSubject
        trans.title = self.enteredTitle.get()
        trans.description = self.enteredDesc.get()
        self.selectedAccount.AddTransaction(trans)
        self.GrowTransactionHistory()
        trans.printData()
        
    def GrowTransactionHistory(self):
        print("transaction history update")
        pass

    def AccountSelect(self, selectedAccount):
        self.accountChoice.set(selectedAccount.name)
        self.balanceDisplay.configure(text = selectedAccount.balance)
        self.selectedAccount = selectedAccount
        self.GrowTransactionHistory()


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

        yScrollBar = ttk.Scrollbar(orient = "vertical", command = tree.yview)
        tree.configure(yscrollcommand = yScrollBar.set)

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
        bankAccount = Account.Account()
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
