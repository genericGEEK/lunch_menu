# lunch_menu
Nutrislice school menu to Google Calendar event

## Description
This project was created to integrate with the Nutrislice school lunch menu service and create Google Calendar events.  
These calendar events are then fed into my DAK Board display at home.  DAK Board has direct integration with Nutrislice but I didn't like how it was displayed and prefered how the Google Calendar events were displayed instead.

## Installation
1. Enable a Google Calendar API and Service Account.  Once that's all setup, download the secret file.  I named mine sa_secret_file.json and put it into the Secret directory.
2. Clone the repo
   ```sh
   git clone https://github.com/genericGEEK/lunch_menu.git
   ```
3. Install packages from requirements.txt
4. Create a config.py file in the Secret directory that like this
   ```sh
   # Nutrislice Variables
    COUNTY_NAME = 'SCHOOL_COUNTY_FROM NUTRISLICE_URL'
    MENU_TYPE = 'lunch'

    # Google Calendar API Variables
    SCOPE = ['https://www.googleapis.com/auth/calendar.events']
    SERVICE_ACCOUNT_EMAIL = 'SERVICE_ACCOUNT_EMAIL'
    CLIENT_SECRET_FILE = 'secret/sa_secret_file.json'

    # Child Variables
    KIDS = {
        'CHILD_NAME': {
            'school_name': 'SCHOOL_NAME',
            'school_id': 'SCHOOL_NAME_FROM_NUTRISLICE_URL',
            'calendar_id': 'GOOGLE_CALENDAR_ID'
        },
        'CHILD_NAME': {
            'school_name': 'SCHOOL_NAME',
            'school_id': 'SCHOOL_NAME_FROM_NUTRISLICE_URL',
            'calendar_id': 'GOOGLE_CALENDAR_ID'
        }
    }
   ```

## Credits
I got the base code for the menu scraper from [hpa_menu_package](https://github.com/zekesarosi/hpa_menu_package/tree/main) and then altered it to get the exact data I wanted.  
