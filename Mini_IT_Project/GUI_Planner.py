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
        self.transCalendar = Calendar(self.calendarFrame, 
                                      font = "Arial 30", selectmode = 'day', cursor = "hand2", 
                                      year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)

        self.transCalendar.grid(row = 0, column = 0)

        self.calendarFrame.place(x = 75, y = 75)

    def InitTimeEntry(self):

        self.timePickerFrame = Frame(master = self.parent)

        self.LTime = Label(master = self.parent, text = "Time:")

        self.timePickerFrame.place(relx = 0.91, y = 75, anchor = "ne")


        self.previousTime = ["0", "0", "0"]
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
            self.SVTime[i].set("0")
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

            


        