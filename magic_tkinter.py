import time
from tkinter import *
import datetime as dt
import locale
from random import randint
# import google_calendar.calendar_google as gg
# import microsoft_to_do_list.to_do_list as to_do

import quotes
from models.calendar_model import Calendar
from calendar import calendar
import json

from models.to_do_list_model import ToDoList
from microsoft_to_do_list.ricorda_di_task import ricorda_di_task
from microsoft_to_do_list.routine_task import routine_task

locale.setlocale(locale.LC_ALL, 'it_IT')

# --------------------------------------------- VARIABLES ----------------------------------------------------

CLIENT_FILE = "google_calendar/credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.events.readonly"]

now = dt.datetime.now()
clock = now.strftime("%H:%M:%S")
date = now.strftime("%A, %d %B")
count = 0
row_number = 0
size = 14
calendar_m = Calendar(calendar)
ricorda_di_list = ToDoList(ricorda_di_task).title_list
routine_list = ToDoList(routine_task).title_list


# ------------------------------------------ Tkinter WINDOW -------------------------------------------------

window = Tk()
window.title("Isabelle's Magic Mirror")
window.geometry("1400x750")
window.config(bg="black", padx=25, pady=25)


# -------------------------------------------- FUNCTIONS -------------------------------------------------

def clock_func():
    '''Display a digital clock'''
    global date
    date_time = dt.datetime.now().strftime("%A, %d %B  %H:%M:%S/")
    date, time1 = date_time.split("  ")
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    time = time2 + ' ' + time3
    clock_label.config(text=time)
    date_label.config(text=date)
    clock_label.after(1000, clock_func)


def change_quote():
    '''Choose a random motivational quote'''
    quote = quotes.quotes[randint(1, len(quotes.quotes) - 1)]
    q_text = quote["text"]
    q_author = quote["author"]
    quote_text_label.config(text=q_text)
    # quote_text_label.grid_configure(row=3, column=1, padx=50, pady=(20, 0), columnspan=3)
    quote_author_label.config(text=q_author)
    # quote_author_label.grid(row=4, column=1, padx=50, pady=(0, 20), columnspan=3)
    # TODO: after midnight this function choose a new random quote

    # hour, minutes, seconds = now.time().strftime("%H:%M:%S").split(':')
    # if int(hour) == int("20") and int(minutes) == int("57") and int(seconds) == int("00"):
    # now = dt.datetime.now().time()
    # today00 = now.replace(hour=11, minute=33, second=0, microsecond=0)
    # if now > today00:
    #     def func():
    #         new_quote = quotes.quotes[randint(1, len(quotes.quotes) - 1)]
    #         quote_text_label.config(text=new_quote["text"])
    #         quote_author_label.config(text=new_quote["author"])
    # # if dt.datetime.now().time() == dt.datetime.now().time().replace():
    # #     quote_text_label.after(0, change_quote)
    #     quote_text_label.after(1000, func)


def move_quote():
    '''Move quote text and author to the top of the screen'''
    quote_text_label.grid_configure(row=0)
    quote_author_label.grid_configure(row=1)


def contract_greet():
    '''Animating greet label by increasing its size'''
    global count, size
    if count <= 10 and count > 0:
        size -= 2
        greet_label.config(font=("Ariel", size))
        count -= 1
        window.after(100, contract_greet)


def expand_greet():
    '''Animating greet label by decreasing its size'''
    global count, size
    if count < 10:
        size += 2
        greet_label.config(font=("Ariel", size))
        count += 1
        window.after(100, expand_greet)
    elif count == 10:
        time.sleep(2)
        window.after(100, contract_greet)


def destroy_greet():
    '''Destroy greet label'''
    greet_label.destroy()


# -------------------------------------------------- GUI ---------------------------------------------------

clock_label = Label(text=clock, fg="white", bg="black", anchor="nw", font=("Ariel", 40, "bold"))
clock_label.grid(row=row_number, column=0, padx=20, pady=(20, 0))
date_label = Label(text=date, fg="white", bg="black", font=("Ariel", 20, "normal"))
date_label.grid(row=row_number+1, column=0, padx=20)

greet_label = Label(text="Ciao Isabelle Michelle", fg="white", bg="black", font=("Ariel", 20, "normal"), anchor="center", width=50)
greet_label.grid(row=4, column=1, padx=50, pady=20)

quote_text_label = Label(text="", wraplength=500, fg="white", bg="black", justify="center", font=("Ariel", 20, "normal"), width=50)
quote_author_label = Label(text="", fg="white", bg="black", justify="center", font=("Ariel", 15, "normal"), width=50)
quote_text_label.grid(row=5, column=1, padx=50, columnspan=3)
quote_author_label.grid(row=6, column=1, padx=50, columnspan=3)

weather_label = Label(text="SUN", fg="white", bg="black", justify="right", font=("Ariel", 20, "normal"))
weather_label.grid(row=row_number, column=4, padx=50, sticky="E")
# sentence = Label(text=motivational_sentences[randint(0, len(motivational_sentences) - 1)], wraplength=400, fg="white", bg="black", font=("Ariel", 20, "normal"))
# sentence.grid(row=3, column=1)

for i in range(0,4):
    number_weekday = str(calendar_m.date_number[i]) + " " +  str(calendar_m.weekday[i])
    hour_name = str(calendar_m.hour[i]) + "     " + str(calendar_m.name[i])
    i += 1
    s = str(f"{number_weekday}\n{hour_name}")

    number = Label(text=s, fg="white", bg="black", font=("Ariel", 15))
    number.grid(row=i+1, column=0, sticky="nw")
    row_number += i
    # hour = Label(text=hour_name, fg="white", bg="black", anchor="sw", font=("Ariel", 15))
    # hour.grid(row=i+1, column=0)
    # weekday = Label(text=calendar_m.weekday[i], fg="white", bg="black", anchor="nw", font=("Ariel", 15))
    # weekday.grid(row=2, column=1)
    # hour = Label(text=calendar_m.hour[i], fg="white", bg="black", anchor="nw", font=("Ariel", 15))
    # hour.grid(row=3, column=0)
    # title = Label(text=calendar_m.name[i], fg="white", bg="black", anchor="nw", font=("Ariel", 15))
    # title.grid(row=4, column=1)

print(routine_list)
routine_title_label = Label(text="Routine:", fg="white", bg="black", font=("Ariel", 15, "bold"))
routine_title_label.grid(row=row_number+1, column=0, pady=(20, 5), sticky="w")

for i in range (len(routine_list)):
    routine_label = Label(text=f"☐   {routine_list[i]}", fg="white", bg="black", font=("Ariel", 15))
    i += 1
    routine_label.grid(row=row_number + 1 + i, column=0, sticky="w")
    row_number += i

ricorda_title_label = Label(text="Ricorda di:", fg="white", bg="black", font=("Ariel", 15, "bold"))
ricorda_title_label.grid(row=row_number+2, column=0, pady=(20,5), sticky="w")

for i in range (len(ricorda_di_list)):
    ricorda_di_label = Label(text=f"☐   {ricorda_di_list[i]}", fg="white", bg="black", font=("Ariel", 15))
    i += 1
    ricorda_di_label.grid(row=row_number+2+i, column=0, sticky="w")
    row_number += i


clock_func()
# expand_greet()
window.after(4000, destroy_greet)
quote_text_label.after(4025, change_quote)
quote_text_label.after(10000, move_quote)

# gg.main(CLIENT_FILE, SCOPES)

window.mainloop()
