# Raven
from tkinter import Frame, Label, Button, StringVar, Entry
from tkcalendar import Calendar
import Constants
import datetime
import Plans

class GUI_Planner:

    def __init__(self, parent: Frame):
        self.parent = parent

        # self.plannerDesc = Label(master = parent, text = "This platform all about your budget planner", font = ("", 12), bg = Constants.mainWindowBgColor)
        # self.plannerDesc.place(relx = 0.5 , rely = 0, anchor = "n")
        # self.plannerDesc2 = Label(master = parent, text = "\'The safe way to double your money is to fold it over once and put it in your pocket\'", font = ("", 12), bg = Constants.mainWindowBgColor)
        # self.plannerDesc2.place(relx = 1.0, rely = 1.0, anchor = "se")
        
        self.InitCalendar()
        self.InitTimeEntry()

        pass

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

        self.timePickerFrame = Frame(master = self.parent)
        self.timePickerFrame.place(relx = 0.91, y = 75, anchor = "ne")

        self.LTime = Label(master = self.parent, text = "Start Time:")
        self.LTime.place(relx = 0.62, y = 55, anchor = "nw")

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



        self.timePickerFrame2 = Frame(master = self.parent)
        self.timePickerFrame2.place(relx = 0.91, y = 225, anchor = "ne")

        self.LTime2 = Label(master = self.parent, text = "End Time:")
        self.LTime2.place(relx = 0.62, y = 205, anchor = "nw")

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
    
    def VerifyDTDiff(self):
        self.RetrieveDateTime()
        if self.rEndDT < self.rStartDT:
            for i in self.EntryTime:
                i.configure(fg = "red")
            for i in self.EntryTime2:
                i.configure(fg = "red")
            ######################## PUT BUTTON UNABLE TO CLICK ###############################
        else:
            for i in self.EntryTime:
                i.configure(fg = "black")
            for i in self.EntryTime2:
                i.configure(fg = "black")


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