from APIs import nutrislice as menu, google_cal
from secret.config import *
from helpers.helpers import *


date = get_current_date()
client = google_cal.GoogleCalendarClient()
new_value = ''

def main():
    for name, var in KIDS.items():
        print('Collecting menu for', var['school_name'])
        menu_list = menu.collect_month(date, var['school_id'])
        print('Menu collection complete, sending to Google Calendar')
        count = 0
        for week in menu_list:
            for day in week:
                count += 1
                summary = day['summary']
                desc = day['description']
                start_date = day['start']
                start = start_date['date']
                end_date = day['end']
                end = end_date['date']
                client.create_event(summary, desc, start, end, calendar_id=var['calendar_id'])
        print('Sent {} meals to Google Calendar'.format(count))


if __name__ == '__main__':
    main()
