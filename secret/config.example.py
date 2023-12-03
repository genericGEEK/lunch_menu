# Nutrislice Variables
#
# URL construction with variables below
# https://{COUNTY_NAME}.api.nutrislice.com/menu/api/weeks/school/{school_id}/menu-type/{MENU_TYPE}/{year}/{month}/{day}
#

COUNTY_NAME = ''
MENU_TYPE = '' # Either 'breakfast' or 'lunch'

# Google Calendar API Variables
SCOPE = ['https://www.googleapis.com/auth/calendar.events']
SERVICE_ACCOUNT_EMAIL = ''
CLIENT_SECRET_FILE = 'secret/sa_secret_file.json' # Json file from Google

# Child Variables - I have 2 kids in different schools
KIDS = {
    'Child 1': {
        'school_name': '', # Casual School Name
        'school_id': '', # School name from url
        'calendar_id': '' # Calendar ID from your Google Calendar
    },
    'Child 2': {
        'school_name': '', # Casual School Name
        'school_id': '', # School name from url
        'calendar_id': '' # Calendar ID from your Google Calendar
    }
}
