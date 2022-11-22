from flask import Flask, render_template
import datetime as dt
import locale
import random
from motivational_sentences import motivational_sentences

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, 'it_IT')

@app.route('/')
def hello_world():
    now = dt.datetime.now()
    clock = now.strftime("%H:%M:%S")
    date = now.strftime("%A, %d %B")
    sentence = motivational_sentences[random.randint(0, len(motivational_sentences) - 1)]
    return render_template("home.html", clock=clock, date=date, sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
