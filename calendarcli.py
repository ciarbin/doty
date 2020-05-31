#Author: Marcin Olko

#TODO:
    #Function for creating events
    #Getting and changing calendar

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetimemanager

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

#Logging into Google Api, loading required token for OAuth2, building calendar service
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
GOOGLECALENDARSERVICE = build('calendar', 'v3', http=creds.authorize(Http()))

def list_events(maxResults = 250, timeMin = None, timeMax = None):
    """
    Function returning list of events ordered by start time from your primary calendar.

    maxResults - int, maximum number of returned elements
    timeMax - Upper bound (exclusive) for an event's start time to filter by.
        Must be an RFC3339 timestamp with mandatory time zone offset,
        for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z
    timeMin - Lower bound (exclusive) for an event's end time to filter by.
        Must be an RFC3339 timestamp with mandatory time zone offset,
        for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z
    If maxResults is not given, it will return 250 first events maching requirements.
    If timeMin is not given, it will get all events ending after current time.
    If timeMax in not given, it will get all events starting after timeMin.
    """

    if timeMin == None:
        timeMin = datetimemanager.from_time_to_RFC3339()
    events_result = GOOGLECALENDARSERVICE.events().list(
        calendarId='primary',
        timeMin=timeMin,
        timeMax=timeMax,
        maxResults=maxResults,
        singleEvents=True,
        orderBy='startTime',
    ).execute()
    events = events_result.get('items', [])

    return events
