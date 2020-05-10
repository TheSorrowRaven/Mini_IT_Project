# Raven
from tkinter import Frame, Label, Button, StringVar, Entry, OptionMenu
from tkcalendar import Calendar
import Constants as Constants
import datetime
import Plans as Plans
import Interfaces as Interfaces

class GUI_Planner(Interfaces.IOnSave):

    def OnSave(self):
        self.main.SaveData("plans", self.Plans)

    def __init__(self, parent: Frame, main):
        super().__init__(main)
        self.main = main
        self.parent = parent

        # self.plannerDesc = Label(master = parent, text = "This platform all about your budget planner", font = ("", 12), bg = Constants.mainWindowBgColor)
        # self.plannerDesc.place(relx = 0.5 , rely = 0, anchor = "n")
        # self.plannerDesc2 = Label(master = parent, text = "\'The safe way to double your money is to fold it over once and put it in your pocket\'", font = ("", 12), bg = Constants.mainWindowBgColor)
        # self.plannerDesc2.place(relx = 1.0, rely = 1.0, anchor = "se")
        

        plans = main.GetSavedData("plans")
        if (plans is None):
            self.Plans = Plans.Plans()
        else:
            self.Plans = plans

        self.EFrame = Frame(master = self.parent)
        self.EFrame.place(relx = 0.65, rely = 0.1, anchor = "nw")

        self.InitCalendar()
        self.InitTimeEntry()
        self.InitDetailsEntry()
        self.InitSyncGC()

    def InitSyncGC(self):
        def Sync():
            self.Plans.AddAllPlans()
        self.syncButton = Button(master = self.parent, text = "Sync plans with Google Calendar", command = Sync)
        self.syncButton.place(relx = 1, rely = 1, anchor = "se")

    def InitCalendar(self):

        self.calendarFrame = Frame(master = self.parent)

        #Calendar
        self.LCalendar     = Label(master = self.calendarFrame, text = "Date:", bg = Constants.mainWindowAltColor)
        self.planCalendar = Calendar(self.calendarFrame, 
                                      font = "Arial 30", selectmode = 'day', cursor = "hand2", 
                                      year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)

        self.planCalendar.grid(row = 0, column = 0)

        self.calendarFrame.place(x = 75, y = 75)

    def InitTimeEntry(self):

        self.timePickerFrame = Frame(master = self.EFrame)
        self.timePickerFrame.grid(row = 0, column = 1)

        self.LTime = Label(master = self.EFrame, text = "Start Time:")
        self.LTime.grid(row = 0, column = 0)

        self.previousTime = ["08", "00", "00"]
        self.SVTime = [StringVar(), StringVar(), StringVar()]
        self.EntryTime = [None] * 3
        self.LsplitTime = [
            Label(master = self.timePickerFrame, text = "  Hour  "),
            Label(master = self.timePickerFrame, text = " Minute "),
            Label(master = self.timePickerFrame, text = " Second ")]
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



        self.timePickerFrame2 = Frame(master = self.EFrame)
        self.timePickerFrame2.grid(row = 1, column = 1)

        self.LTime2 = Label(master = self.EFrame, text = "End Time:")
        self.LTime2.grid(row = 1, column = 0)

        self.previousTime2 = ["16", "0", "0"]
        self.SVTime2 = [StringVar(), StringVar(), StringVar()]
        self.EntryTime2 = [None] * 3
        self.LsplitTime2 = [
            Label(master = self.timePickerFrame2, text = "  Hour  "),
            Label(master = self.timePickerFrame2, text = " Minute "),
            Label(master = self.timePickerFrame2, text = " Second ")]
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
        self.detailsFrame = Frame(master = self.EFrame)
        self.detailsFrame.grid(row = 2, column = 1, pady = (10, 5))

        parent = self.detailsFrame

        self.LTitle = Label(master = parent, text = "Title:")
        self.LTitle.grid(row = 0, column = 0)
        self.SVTitle = StringVar()
        self.ETitle = Entry(master = parent, textvariable = self.SVTitle)
        self.ETitle.grid(row = 0, column = 1, columnspan = 2, padx = (0,2))

        self.LLocation = Label(master = parent, text = "Location:")
        self.LLocation.grid(row = 1, column = 0)
        self.SVLocation = StringVar()
        self.ELocation = Entry(master = parent, textvariable = self.SVLocation)
        self.ELocation.grid(row = 1, column = 1, columnspan = 2, padx = (0,2))

        self.LDesc = Label(master = parent, text = "Description:")
        self.LDesc.grid(row = 2, column = 0)
        self.SVDesc = StringVar()
        self.EDesc = Entry(master = parent, textvariable = self.SVDesc)
        self.EDesc.grid(row = 2, column = 1, columnspan = 2, padx = (0,2))

        self.LFreq = Label(master = parent, text = "Count & Frequency:")
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