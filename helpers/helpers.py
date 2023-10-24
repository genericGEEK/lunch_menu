from datetime import datetime


def get_current_date():
    currentMonth = str(datetime.now().month)
    currentYear = str(datetime.now().year)
    date = currentYear + '-' + currentMonth
    return date
