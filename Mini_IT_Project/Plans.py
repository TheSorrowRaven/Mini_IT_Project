# Raven

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Plans():


    def __init__(self):
        self.plans = []

    def InitGCalendar(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
                
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    def AddPlan(self, title, location, description, frequency, startDT, endDT, count):
        plan = Plan()
        plan.title = title
        plan.location = location
        plan.description = description
        plan.frequency = frequency
        plan.startDT = startDT
        plan.endDT = endDT
        plan.count = count

        self.plans.append(plan)

        print(self.plans)

    def AddAllPlans(self):
        self.InitGCalendar()
        for i in self.plans:
            if not i.added:
                i.service = self.service
                i.SetGEvent()

    


class Plan():

    added = False
    title = ""
    location = ""
    description = ""
    frequency = "MONTHLY"
    count = 1

    def __init__(self):
        self.startDT = None
        self.endDT = None
        self.service = None

    def SetGEvent(self):

        startTime = self.startDT.strftime("%Y-%m-%dT%H:%M:%S")
        endTime = self.endDT.strftime("%Y-%m-%dT%H:%M:%S")

        event = {
        'summary': self.title,
        'location': self.location,
        'description': self.description,
        'start': {
            'dateTime': startTime,
            'timeZone': 'Asia/Kuala_Lumpur',
        },
        'end': {
            'dateTime': endTime,
            'timeZone': 'Asia/Kuala_Lumpur',
        },
        'recurrence': [
            'RRULE:FREQ='+ self.frequency +';COUNT=' + self.count
        ],
        'reminders': {
            'useDefault': True
        },
        }

        try:
            event = self.service.events().insert(calendarId='primary', body=event).execute()
            self.added = True
            print ('Event created: %s' % (event.get('htmlLink')))
        except Exception as e:
            print(e)
        

        
if __name__ == "__main__":
    print("Please run main.py instead")
    pass