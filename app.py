from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kontakt.html')
def kontakt():
    return render_template("kontakt.html")

@app.route('/meny.html')
def meny():
    return render_template("meny.html",
                           day = datetime.datetime.now(),
                           dag = {
                               "Monday" : {
                               "knekkebrød", "brød", "leverpostei", "kaviar", "ost"
                               },
                           "Tuesday" : {
                               "1. knekkebrød", "2. brød", "3. jordbær syltetøy", "4. bringebær syltetøy", "5. skinke"
                               },
                           "Wednesday" : {
                               "1. knekkebrød", "2. brød", "3. salami", "4. brunost", "5. ost"
                               },
                           "Thursday" : {
                               "1. knekkebrød", "2. brød", "3. smør", "4. skinke", "5. kaviar"
                               },
                           "Friday" : {
                               "1. knekkebrød", "2. brød", "3. kaviar", "4. makrellitomat", "5. sursild"
                               }
                           })

@app.route('/varer.html')
def varer():
    return render_template("varer.html")

if __name__ == "__main__":
    app.run()