import json
import requests
from secret.config import *


def save(data, file_name):
    with open(file=file_name, mode='w') as file:
        json.dump(data, file, indent=4)


def check_len(month, year):
    months = {"0" + str(month) if len(str(month)) < 2 else str(month) for month in range(1, 13)}
    three_months = {"04", "06", "09", "11"}
    three_one_months = months - three_months - {"02"}
    month = "0" + str(month) if len(str(month)) < 2 else str(month)
    if month in months and month in three_one_months:
        return 31
    if month in months and month in three_months:
        return 30
    if month == "02":
        if int(year) % 4 == 0:
            return 29
        else:
            return 28


def collect_month(date, school_id, full_week=False):
    month_specified = date.split("-")[1]
    date += "-01"
    year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
    start_menu = collect_week(f"{year}-{month}-{day}", school_id)
    menu_dict = {}
    menu_list = [start_menu]
    cycling = True
    while cycling:
        day = ("0" + str(int(day) + 7) if int(day) < 3 else int(day) + 7)
        week_menu = collect_week(f"{year}-{month}-{day}", school_id)
        menu_list.append(week_menu)
        if int(day) >= check_len(month, year):
            cycling = False
    res = []
    [res.append(x) for x in menu_list if x not in res]

    return res


def request(url):
    try:
        data = requests.get(url)
        return data.json()
    except:
        print(f"Invalid Url, Response Code: {data.status_code}. Probable that was an invalid date")
        exit()


def collect_week(date, school_id):
    url = week_url(date, school_id)
    data = request(url)
    menudict = dataparser(data)
    return menudict


def week_url(date, school_id):
    date = date.split("-")
    year, month, day = date[0], date[1], date[2]
    url = rf"https://{COUNTY_NAME}.api.nutrislice.com/menu/api/weeks/school/{school_id}/menu-type/{MENU_TYPE}/{year}/{month}/{day}"
    return url


def dataparser(data):
    results_filtered_list_of_dict = []
    for day in data['days']:
        if len(day['menu_items']) != 0:
            date = day['date']
            sidelist = []
            first = True
            for info in day['menu_items']:
                results_filtered_dict = {}
                if len(info['text']) > 1:
                    entree = 'No School'
                    sidelist.append(info['text'])
                else:

                    food_dict = info['food']
                    if food_dict is not None:
                        food = food_dict['name']
                        if first:
                            entree = food

                            first = False
                        else:
                            sidelist.append(food)
            results_filtered_dict['summary'] = entree
            filtered_sidelist = str(sidelist)[1:-1]
            results_filtered_dict['description'] = filtered_sidelist.replace("'", '')
            results_filtered_dict['start'] = {
                'date': date
            }
            results_filtered_dict['end'] = {
                'date': date
            }
            results_filtered_list_of_dict.append(results_filtered_dict)
    return results_filtered_list_of_dict