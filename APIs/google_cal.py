import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from secret.config import *


class GoogleCalendarClient:
    """ Client for Google Calendar API """

    def __init__(self, *args, **kwargs):
        self.scopes = kwargs.get('scopes', SCOPE)
        self.client_secrete_file = kwargs.get('client_secrete_file',
                                              CLIENT_SECRET_FILE)
        self.default_calendar_id = kwargs.get('calendar_id')
        self.service = self._build_service()

    def _get_credintials(self):
        return Credentials.from_service_account_file(self.client_secrete_file,
                                                     scopes=self.scopes)

    def _build_service(self):
        return build('calendar', 'v3',
                     credentials=self._get_credintials())

    def _format_datetime(self, datetime_object):
        formatted_datetime = datetime_object.isoformat(timespec='seconds')
        if not datetime_object.utcoffset():
            formatted_datetime += 'Z'
        return formatted_datetime

    def get_events(self, calendar_id=None, **kwargs):
        if calendar_id is None:
            calendar_id = self.default_calendar_id

        now = datetime.datetime.utcnow()
        time_delta = datetime.timedelta(days=30)
        time_min = self._format_datetime(now - time_delta)
        time_max = self._format_datetime(now + time_delta)

        if kwargs.get('search_text'):
            query = kwargs.get('search_text')
        else:
            query = None

        response = self.service.events().list(calendarId=calendar_id,
                                              q=query,
                                              timeMin=time_min,
                                              timeMax=time_max,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        return response.get('items', [])

    def create_event(self, summary, desc, start, end, calendar_id=None):
        if calendar_id is None:
            calendar_id = self.default_calendar_id

        body = {
            'summary': summary,
            'description': desc,
            'start': {
                #'date': self._format_datetime(start),
                'date': start
              },
            'end': {
                'date': end,
              },
         }
        return self.service.events().insert(calendarId=calendar_id,
                                            body=body).execute()