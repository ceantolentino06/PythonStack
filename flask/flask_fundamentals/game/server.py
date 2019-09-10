from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/safe")
def safe():
    return render_template('safe.html')

@app.route("/fast")
def notsafe():
    return render_template('fast.html')

@app.route("/shiny")
def shiny():
    return render_template('shiny.html')

@app.route("/liquid")
def liquid():
    return render_template('liquid.html')

@app.route("/run")
def run():
    return render_template('run.html')

@app.route("/sneak")
def sneak():
    return render_template('sneak.html')

@app.route("/death1")
def death1():
    return render_template('death1.html')

@app.route("/death2")
def death2():
    return render_template('death2.html')


if(__name__=="__main__"):
    app.run(debug=True)