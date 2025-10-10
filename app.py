from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kontakt.html')
def kontakt():
    return render_template("kontakt.html")

@app.route('/meny.html')
def meny():
    return render_template("meny.html", varm=input("hva er dagen's varmmat: "))

@app.route('/varer.html')
def varer():
    return render_template("varer.html")

if __name__ == "__main__":
    app.run()