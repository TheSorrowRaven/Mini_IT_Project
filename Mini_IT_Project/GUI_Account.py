# Raven
from tkinter import Frame, ttk, Entry, Button, StringVar
import Constants
import Interfaces
import Account

class GUI_Account(Interfaces.IOnSave):

    accounts = []
    categories = []

    def OnSave(self):
        self.Main.SaveData("AccountsList", self.accounts)
        self.Main.SaveData("CategoriesList", self.categories)

    def __init__(self, parent: Frame, main):
        self.Main = main
        self.parent = parent
        super().__init__(main)
        self.accounts = main.GetSavedData("AccountsList")
        self.categories = main.GetSavedData("CategoriesList")
    
        if (self.accounts is None):
            self.NewUserAccounts()
        else:
            self.LoadAccounts()
        if (self.categories is None):
            self.NewUserCategories()
        else:
            self.LoadCategories()

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
                self.addCategoryButton.place(relx = 0.9, rely = 1, anchor = "se")
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
        self.addCategoryEntry.bind("<Enter>", lambda e: ButtonCreateCategory())

        self.addCategoryButton = Button(master = self.categoryFrame, text = "+", command = ButtonCreateCategory)
        

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
        self.accounts.append(cashAccount)

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
