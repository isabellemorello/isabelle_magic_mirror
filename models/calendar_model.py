import datetime as dt
import  locale
from calendar import calendar
import json

locale.setlocale(locale.LC_ALL, 'it_IT')

class Calendar:
    def __init__(self, cal):
        self.calendar = cal
        self.name = self.get_name()
        self.date = self.get_date()
        self.date_number = self.get_date_number()
        self.weekday = self.get_date_weekday()
        self.month = self.get_date_month()
        self.hour = self.get_hour()

    def get_dateTime_and_name(self):
        calendar_list = []
        for event in calendar:
            dateStart = event["start"]
            summary = event["summary"]
            for key,value in dateStart.items():
                if key == "dateTime":
                    cal_event = {summary : value}
                    calendar_list.append(cal_event)
        # print(calendar_list)
        return calendar_list


    def get_name(self):
        event_name = []
        calendar_list =  self.get_dateTime_and_name()
        for e in calendar_list:
            for key, value in e.items():
                event_name.append(key)
        # print(event_name)
        return event_name


    def get_date(self):
        event_date = []
        date = []
        calendar_list = self.get_dateTime_and_name()
        for e in calendar_list:
            for key,value in e.items():
                event_date.append(value)
        print(event_date)

        for d in event_date:
            dateTime = str(d[0:10]).split("-")
            date.append(dt.date(day=int(dateTime[2]), month=int(dateTime[1]), year=int(dateTime[0])))
        # print(date)
        return date

    def get_date_number(self):
        number_list = []
        date = self.get_date()
        for d in date:
            number_list.append(d.day)
        # print(number_list)
        return number_list


    def get_date_weekday(self):
        weekday_list = []
        date = self.get_date()
        for wd in date:
            weekday_list.append(wd.strftime("%A"))
        # print(weekday_list)
        return weekday_list


    def get_date_month(self):
        month_list = []
        date = self.get_date()
        for m in date:
            month_list.append(m.strftime("%b"))
        # print(month_list)
        return month_list


    def get_hour(self):
        # dateTime = self.get_dateTime_and_name()
        dateTime = "2022-11-21T10:30:00+01:00"
        h = dateTime[11:19].split(":")
        hour = dt.time(hour=int(h[0]), minute=int(h[1]), second=int(h[2])).strftime("%H:%M")
        # print(hour)
        return hour


c = Calendar(calendar)
for i in range(0,5):
    i += 1
    print(f"Hai un evento: {c.name[i]}, {c.weekday[i]} {c.date_number[i]} {c.month[i]} alle ore {c.hour}")