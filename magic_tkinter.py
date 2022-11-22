import time
from tkinter import *
import datetime as dt
import locale
from random import randint
# import google_calendar.calendar_google as gg
# import microsoft_to_do_list.to_do_list as to_do

import quotes


locale.setlocale(locale.LC_ALL, 'it_IT')

# --------------------------------------------- VARIABLES ----------------------------------------------------

CLIENT_FILE = "google_calendar/credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.events.readonly"]

now = dt.datetime.now()
clock = now.strftime("%H:%M:%S")
date = now.strftime("%A, %d %B")
count = 0
size = 14


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
clock_label.grid(row=0, column=0, padx=20, pady=(20, 0))
date_label = Label(text=date, fg="white", bg="black", font=("Ariel", 20, "normal"))
date_label.grid(row=1, column=0, padx=20, pady=(0, 20))

greet_label = Label(text="Ciao Isabelle Michelle", fg="white", bg="black", font=("Ariel", size, "normal"), anchor="center")
greet_label.grid(row=3, column=1, padx=50, pady=20)

quote_text_label = Label(text="", wraplength=500, fg="white", bg="black", justify="center", font=("Ariel", 20, "normal"), width=50)
quote_author_label = Label(text="", fg="white", bg="black", justify="center", font=("Ariel", 15, "normal"), width=50)
quote_text_label.grid(row=5, column=1, padx=50, pady=(20, 0), columnspan=3)
quote_author_label.grid(row=6, column=1, padx=50, pady=(0, 20), columnspan=3)

weather_label = Label(text="SUN", fg="white", bg="black", justify="right", font=("Ariel", 20, "normal"))
weather_label.grid(row=0, column=4, padx=50, pady=20, sticky="E")
# sentence = Label(text=motivational_sentences[randint(0, len(motivational_sentences) - 1)], wraplength=400, fg="white", bg="black", font=("Ariel", 20, "normal"))
# sentence.grid(row=3, column=1)




clock_func()
expand_greet()
window.after(4000, destroy_greet)
quote_text_label.after(4025, change_quote)
quote_text_label.after(10000, move_quote)

# gg.main(CLIENT_FILE, SCOPES)

window.mainloop()
