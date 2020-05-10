from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Plans():

    def __init__(self):

        self.InitGCalendar()

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
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

class Plan():

    title = ""
    location = ""
    description = ""
    frequency = "MONTHLY"

    def __init__(self, service):
        self.startDT = None
        self.endDT = None
        self.stopDT = None
        self.service = service

    def SetGEvent(self):

        self.stopDT = self.stopDT - datetime.timedelta(hours=8)

        startTime = self.startDT.strftime("%y-%m-%dT%H:%M:%S")
        endTime = self.endDT.strftime("%y-%m-%dT%H:%M:%S")
        stopTime = datetime.datetime().now().strftime("%y%m%dT%H%M%SZ")

        event = {
        'summary': self.title,
        'location': self.location,
        'description': self.description,
        'start': {
            'dateTime': startTime,
            'timeZone': 'Malaysia',
        },
        'end': {
            'dateTime': endTime,
            'timeZone': 'Malaysia',
        },
        'recurrence': [
            'RRULE:FREQ='+ self.frequency +';UNTIL=' + stopTime
        ],
        'reminders': {
            'useDefault': True
        },
        }

        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print ('Event created: %s' % (event.get('htmlLink')))