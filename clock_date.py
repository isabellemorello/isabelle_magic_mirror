import datetime as dt
import locale

from tkinter import *
from tkinter.ttk import *

locale.setlocale(locale.LC_ALL, 'it_IT')

now = dt.datetime.now()
clock = now.strftime("%H:%M")
date = now.strftime("%A, %d %B")
print(clock)


window = Tk()
window.title("Clock")
window.geometry('500x250')

tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
# alarm_tab = Frame(tabs_control)
# stopwatch_tab = Frame(tabs_control)
# timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
# tabs_control.add(alarm_tab, text="Alarm")
# tabs_control.add(stopwatch_tab, text='Stopwatch')
# tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill ="both")

time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')

def clock():
    date_time = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    # if int(hour) > 12 and int(hour) < 24:
    #     time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    # else:
    time = time2 + ' ' + time3
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)

clock()

import requests

response = requests.get(url="https://type.fit/api/quotes")
quotes = response.text
with open("quotes.json", "w") as quote:
    quote.write(f"quotes = {quotes}")
window.mainloop()