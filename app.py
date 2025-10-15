from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/meny.html')
def meny():
    return render_template("meny.html",
                           day = datetime.datetime.now(),
                           dag = {
                            "Monday" : {
                               "knekkebrød", "brød", "leverpostei", "kaviar", "ost"
                               },
                           "Tuesday" : {
                               "knekkebrød", "brød", "jordbær syltetøy", "bringebær syltetøy", "skinke"
                               },
                           "Wednesday" : {
                               "knekkebrød", "brød", "salami", "brunost", "ost"
                               },
                           "Thursday" : {
                               "knekkebrød", "brød", "smør", "skinke", "kaviar"
                               },
                           "Friday" : {
                               "knekkebrød", "brød", "kaviar", "makrellitomat", "sursild"
                               }
                           })

@app.route('/varer.html')
def varer():
    return render_template("varer.html")

@app.route('/kontakt.html')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run()
    
    







"""vare = {
    "sjokomelk": {
        "pris: ": "100"
    },
    "yoghurt": {
        "vanilje": {"pris: ": 100}, 
        "jordbær": {"pris: ": 100},
        "skogsbær": {"pris: ": 100}
    },
    "brus": {
        "cola zero": {"pris: " : 100},
        "cola": {"pris: " : 100},
        "sprite": {"pris: " : 100},
        "fanta": {"pris: " : 100}
    }
}"""