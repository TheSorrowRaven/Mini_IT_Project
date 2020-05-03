# Raven
from tkinter import Frame, ttk
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

        self.displayCategoryTree = self.GrowCategoryTree(self.parent)
        self.displayCategoryTree.place(relx = 1, rely = 1, anchor = "se")

    def NewUserCategories(self):
        self.categories = []
        self.categoryShopping = Account.Category("Shopping")
        self.categories.append(self.categoryShopping)
        self.categories.append(Account.Category("Other"))
        self.categories.append(Account.Category("Clothing", self.categoryShopping))

    def LoadCategories(self):
        pass

    def GrowCategoryTree(self, parent):
        categoryTree = ttk.Treeview(parent)
        categoryTree.heading("#0", text = "Categories")

        def NestCategory(category, parent):
            categoryTree.insert(parent.name, "end",category.name, text = category.name)
        def BaseCategory(category):
            categoryTree.insert("", "end", category.name, text = category.name)
        for i in self.categories:
            if (i.parent is None):
                BaseCategory(i)
            else:
                NestCategory(i, i.parent)

        return categoryTree

    def LoadAccounts(self):
        pass

    def NewUserAccounts(self):
        self.accounts = []
        cashAccount = Account.Account()
        self.accounts.append(cashAccount)

    def CreateCategory(self, name, parent: Account.Category = None):
        self.categories = Account.Category(name, parent)