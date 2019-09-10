from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def root():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add2():
    session['counter'] += 1
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)