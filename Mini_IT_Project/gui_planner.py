###
#/***************************************************
#File Name: gui_planner.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###
from tkinter import Frame, Label, Button, StringVar, Entry, OptionMenu, ttk
from tkcalendar import Calendar
import datetime
import constants as Constants
import plans as Plans
import interfaces as Interfaces

class GUI_Planner(Interfaces.IOnSave):

    def OnSave(self):
        self.main.SaveData("plans", self.Plans.plans)

    def __init__(self, parent: Frame, main):
        super().__init__(main)
        self.main = main
        self.parent = parent

        self.Plans = Plans.Plans()
        plans = main.GetSavedData("plans")
        if (plans is not None):
            self.Plans.plans = plans

        self.InputFrame = Frame(master = parent, bg = Constants.mainWindowAltColor)
        self.InputFrame.place(relx = 0.5, y = 75, anchor = "n")

        self.EFrame = Frame(master = self.InputFrame, bg = Constants.mainWindowAltColor)
        self.EFrame.grid(row = 0, column = 1)

        self.InitCalendar()
        self.InitTimeEntry()
        self.InitDetailsEntry()
        self.InitSyncGC()
        self.InitPlans()

    def InitSyncGC(self):
        def Sync():
            self.Plans.AddAllPlans()
            self.RefreshPlans()
        self.syncButton = Button(master = self.parent, text = "Sync plans with\n Google Calendar", command = Sync)
        self.syncButton.place(relx = 1, rely = 1, anchor = "se")

    def InitCalendar(self):

        self.calendarFrame = Frame(master = self.InputFrame, bg = Constants.mainWindowAltColor)

        #Calendar
        self.LCalendar     = Label(master = self.calendarFrame, text = "Date:", bg = Constants.mainWindowAltColor)
        self.planCalendar = Calendar(self.calendarFrame, 
                                      font = "Arial 20", selectmode = 'day', cursor = "hand2", 
                                      year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)

        self.planCalendar.grid(row = 0, column = 0)

        self.calendarFrame.grid(row = 0, column = 0)

    def InitTimeEntry(self):

        self.timePickerFrame = Frame(master = self.EFrame, bg = Constants.mainWindowAltColor)
        self.timePickerFrame.grid(row = 0, column = 1)

        self.LTime = Label(master = self.EFrame, text = "Start Time:", bg = Constants.mainWindowAltColor)
        self.LTime.grid(row = 0, column = 0)

        self.previousTime = ["08", "00", "00"]
        self.SVTime = [StringVar(), StringVar(), StringVar()]
        self.EntryTime = [None] * 3
        self.LsplitTime = [
            Label(master = self.timePickerFrame, text = "  Hour  ", bg = Constants.mainWindowAltColor),
            Label(master = self.timePickerFrame, text = " Minute ", bg = Constants.mainWindowAltColor),
            Label(master = self.timePickerFrame, text = " Second ", bg = Constants.mainWindowAltColor)]
        self.buttonTimeChange = [None] * 6

        def TimeVerify(svi):
            try:
                if (svi == 0):
                    if (int(self.SVTime[svi].get()) >= 24):
                        self.SVTime[svi].set(str(23))
                else:
                    if (int(self.SVTime[svi].get()) >= 60):
                        self.SVTime[svi].set(str(59))
                if (int(self.SVTime[svi].get()) <= -1):
                    self.SVTime[svi].set(str(0))
                    print(self.SVTime[svi].get())
                self.previousTime[svi] = (self.SVTime[svi].get())
            except ValueError:
                self.SVTime[svi].set(self.previousTime[svi])
            self.VerifyDTDiff()

        def ButtonAddMinusTime(id):
            convert3 = id // 2
            
            if (convert3 == 0):
                upperLimit = 23
            else:
                upperLimit = 59

            if (id % 2 == 0):
                if (int(self.SVTime[convert3].get()) < upperLimit):
                    self.SVTime[convert3].set(str(int(self.SVTime[convert3].get()) + 1))
            else:
                if (int(self.SVTime[convert3].get()) > 0):
                    self.SVTime[convert3].set(str(int(self.SVTime[convert3].get()) - 1))

        for i in range(len(self.SVTime)):
            self.SVTime[i].set(self.previousTime[i])
            self.SVTime[i].trace("w", lambda name, index, mode, i = i: TimeVerify(i))
            self.EntryTime[i] = Entry(master = self.timePickerFrame, textvariable = self.SVTime[i])
            
            for z in range(2):
                j = i*2 + z
                self.buttonTimeChange[j] = Button(master = self.timePickerFrame, command = lambda i = j: ButtonAddMinusTime(i))
                if (z == 0):
                    self.buttonTimeChange[j].configure(text = "      +      ")
                    r = 1
                else:
                    self.buttonTimeChange[j].configure(text = "      -      ")
                    r = 3
                self.buttonTimeChange[j].grid(row = r, column = i)

            self.EntryTime[i].grid(row = 2, column = i, padx = (2, 2), pady = (2, 2))
            self.LsplitTime[i].grid(row = 0, column = i)



        self.timePickerFrame2 = Frame(master = self.EFrame, bg = Constants.mainWindowAltColor)
        self.timePickerFrame2.grid(row = 1, column = 1)

        self.LTime2 = Label(master = self.EFrame, text = "End Time:", bg = Constants.mainWindowAltColor)
        self.LTime2.grid(row = 1, column = 0)

        self.previousTime2 = ["16", "0", "0"]
        self.SVTime2 = [StringVar(), StringVar(), StringVar()]
        self.EntryTime2 = [None] * 3
        self.LsplitTime2 = [
            Label(master = self.timePickerFrame2, text = "  Hour  ", bg = Constants.mainWindowAltColor),
            Label(master = self.timePickerFrame2, text = " Minute ", bg = Constants.mainWindowAltColor),
            Label(master = self.timePickerFrame2, text = " Second ", bg = Constants.mainWindowAltColor)]
        self.buttonTimeChange2 = [None] * 6

        def TimeVerify2(svi):
            try:
                if (svi == 0):
                    if (int(self.SVTime2[svi].get()) >= 24):
                        self.SVTime2[svi].set(str(23))
                else:
                    if (int(self.SVTime2[svi].get()) >= 60):
                        self.SVTime2[svi].set(str(59))
                if (int(self.SVTime2[svi].get()) <= -1):
                    self.SVTime2[svi].set(str(0))
                    print(self.SVTime2[svi].get())
                self.previousTime2[svi] = (self.SVTime2[svi].get())
            except ValueError:
                self.SVTime2[svi].set(self.previousTime2[svi])
            self.VerifyDTDiff()

        def ButtonAddMinusTime2(id):
            convert3 = id // 2
            
            if (convert3 == 0):
                upperLimit = 23
            else:
                upperLimit = 59

            if (id % 2 == 0):
                if (int(self.SVTime2[convert3].get()) < upperLimit):
                    self.SVTime2[convert3].set(str(int(self.SVTime2[convert3].get()) + 1))
            else:
                if (int(self.SVTime2[convert3].get()) > 0):
                    self.SVTime2[convert3].set(str(int(self.SVTime2[convert3].get()) - 1))

        for i in range(len(self.SVTime)):
            self.SVTime2[i].set(self.previousTime2[i])
            self.SVTime2[i].trace("w", lambda name, index, mode, i = i: TimeVerify2(i))
            self.EntryTime2[i] = Entry(master = self.timePickerFrame2, textvariable = self.SVTime2[i])
            
            for z in range(2):
                j = i*2 + z
                self.buttonTimeChange2[j] = Button(master = self.timePickerFrame2, command = lambda i = j: ButtonAddMinusTime2(i))
                if (z == 0):
                    self.buttonTimeChange2[j].configure(text = "      +      ")
                    r = 1
                else:
                    self.buttonTimeChange2[j].configure(text = "      -      ")
                    r = 3
                self.buttonTimeChange2[j].grid(row = r, column = i)

            self.EntryTime2[i].grid(row = 2, column = i, padx = (2, 2), pady = (2, 2))
            self.LsplitTime2[i].grid(row = 0, column = i)
    
    def InitDetailsEntry(self):
        self.detailsFrame = Frame(master = self.EFrame, bg = Constants.mainWindowAltColor)
        self.detailsFrame.grid(row = 2, column = 1, pady = (10, 5))

        parent = self.detailsFrame

        self.LTitle = Label(master = parent, text = "Title:", bg = Constants.mainWindowAltColor)
        self.LTitle.grid(row = 0, column = 0)
        self.SVTitle = StringVar()
        self.ETitle = Entry(master = parent, textvariable = self.SVTitle)
        self.ETitle.grid(row = 0, column = 1, columnspan = 2, padx = (0,2))

        self.LLocation = Label(master = parent, text = "Location:", bg = Constants.mainWindowAltColor)
        self.LLocation.grid(row = 1, column = 0)
        self.SVLocation = StringVar()
        self.ELocation = Entry(master = parent, textvariable = self.SVLocation)
        self.ELocation.grid(row = 1, column = 1, columnspan = 2, padx = (0,2))

        self.LDesc = Label(master = parent, text = "Description:", bg = Constants.mainWindowAltColor)
        self.LDesc.grid(row = 2, column = 0)
        self.SVDesc = StringVar()
        self.EDesc = Entry(master = parent, textvariable = self.SVDesc)
        self.EDesc.grid(row = 2, column = 1, columnspan = 2, padx = (0,2))

        self.LFreq = Label(master = parent, text = "Count & Frequency:", bg = Constants.mainWindowAltColor)
        self.LFreq.grid(row = 3, column = 0)

        def VerifyNumber(string):
            if string == "":
                self.previousCount = string
            else:
                try:
                    int(string)
                    self.previousCount = string
                except ValueError:
                    self.SVCount.set(self.previousCount)

        self.previousCount = "1"
        self.SVCount = StringVar()
        self.SVCount.set("1")
        self.SVCount.trace("w", lambda name, index, mode, choice = self.SVCount: VerifyNumber(choice.get()))
        self.ECount = Entry(master = parent, textvariable = self.SVCount, width = 5)
        self.ECount.grid(row = 3, column = 1)


        self.SVFreq = StringVar()
        freqOptions = ["YEARLY", "MONTHLY", "WEEKLY", "DAILY"]
        self.OFreq = OptionMenu(parent, self.SVFreq, *freqOptions)
        self.OFreq.grid(row = 3, column = 2)
        self.SVFreq.set("MONTHLY")

        self.BSubmit = Button(master = parent, text = "Add Plan", command = self.SubmitPlan)
        self.BSubmit.grid(row = 4, column = 0, columnspan = 3, pady = (4, 4))

    def InitPlans(self):
        self.plansFrame = Frame(master = self.parent)
        self.plansFrame.place(relx = 0.5, rely = 0.59, anchor = "n")

        def updateScroll(event):
            self.plansTree.configure(yscrollcommand = self.plansSBY.set)
            self.plansTree.configure(xscrollcommand = self.plansSBX.set)
            

        self.plansTree = ttk.Treeview(master = self.plansFrame, height = 12)
        self.plansSBY = ttk.Scrollbar(master = self.plansFrame, orient = "vertical", command = self.plansTree.yview)
        self.plansSBY.grid(row = 0, column = 1, sticky = "nse")
        self.plansSBX = ttk.Scrollbar(master = self.plansFrame, orient = "horizontal", command = self.plansTree.xview)
        self.plansSBX.grid(row = 1, column = 0, sticky = "wes")
        self.plansTree.bind("<Configure>", updateScroll)

        self.RefreshPlans()

        
    def RefreshPlans(self):
        try:
            self.plansFrame.place_forget()
        except:
            pass
        self.plansTree.delete(*self.plansTree.get_children())

        self.plansFrame.place(relx = 0.5, rely = 0.59, anchor = "n")

        self.plansTree.grid(row = 0, column = 0)

        self.plansTree["columns"] = ("Title", "Start Date", "Location", "Description", "Frequency", "Count", "Added")

        self.plansTree.column("#0", width = 40)
        self.plansTree.column("#1", width = 100)
        self.plansTree.column("#2", width = 200)
        self.plansTree.column("#3", width = 150)
        self.plansTree.column("#4", width = 150)
        self.plansTree.column("#5", width = 100)
        self.plansTree.column("#6", width = 100)
        self.plansTree.column("#7", width = 100)

        self.plansTree.heading("#1", text = "Title")
        self.plansTree.heading("#2", text = "Start Date")
        self.plansTree.heading("#3", text = "Location")
        self.plansTree.heading("#4", text = "Description")
        self.plansTree.heading("#5", text = "Frequency")
        self.plansTree.heading("#6", text = "Count")
        self.plansTree.heading("#7", text = "Added")

        for i in range(0, len(self.Plans.plans)):
            self.GrowPlansTree(self.plansTree, self.Plans.plans[i], i)

    def GrowPlansTree(self, tree, plan: Plans.Plan, index):
        if (plan.startDT == plan.endDT):
            time = plan.startDT.strftime("%d/%m/%Y @ %H:%M:%S")
        else:
            time = plan.startDT.strftime("%d/%m/%Y @ %H:%M:%S - ") + plan.endDT.strftime("%H:%M:%S")
        if plan.added:
            added = "Yes"
        else:
            added = "No"
        tree.insert("", index, text = str(index + 1), values = (plan.title, time, plan.location, plan.description, plan.frequency, plan.count, added))
        
    def SubmitPlan(self):
        title = self.SVTitle.get()
        location = self.SVLocation.get()
        desc = self.SVDesc.get()
        freq = self.SVFreq.get()
        count = self.SVCount.get()

        self.RetrieveDateTime()

        startTime = self.rStartDT
        endTime = self.rEndDT

        self.Plans.AddPlan(title, location, desc, freq, startTime, endTime, count)
        self.Clear()
        self.RefreshPlans()
        
    def Clear(self):
        self.SVTitle.set("")
        self.SVLocation.set("")
        self.SVDesc.set("")
        self.SVFreq.set("MONTHLY")
        self.SVCount.set("1")

    def VerifyDTDiff(self):
        self.RetrieveDateTime()
        if self.rEndDT < self.rStartDT:
            for i in self.EntryTime:
                i.configure(fg = "red")
            for i in self.EntryTime2:
                i.configure(fg = "red")
            self.BSubmit.grid_forget()
        else:
            for i in self.EntryTime:
                i.configure(fg = "black")
            for i in self.EntryTime2:
                i.configure(fg = "black")
            self.BSubmit.grid(row = 4, column = 0, columnspan = 3, pady = (4, 4))


    def RetrieveDateTime(self):
        date = self.planCalendar.selection_get()
        
        startTime = self.ConvertToTime(self.SVTime[0].get(), self.SVTime[1].get(), self.SVTime[2].get())
        endTime = self.ConvertToTime(self.SVTime2[0].get(), self.SVTime2[1].get(), self.SVTime2[2].get())

        self.rStartDT = datetime.datetime.combine(date, startTime)
        self.rEndDT = datetime.datetime.combine(date, endTime)

    def ConvertToTime(self, hour, minute, second):
        return datetime.time(int(hour), int(minute), int(second))


    def CompareStartEndTime(self):
        pass


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
