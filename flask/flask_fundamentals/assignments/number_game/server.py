from flask import Flask, render_template, redirect, session,request
import random

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def root():
    if 'rand' in session:
        pass
    else:
        session['rand'] = random.randint(1, 101)
    print(session['rand'])
    return render_template('index.html', result=session['result'])

@app.route('/guess', methods=['POST'])
def guess():
    print(request.form)
    if session['rand'] == int(request.form['usernum']):
        session['result'] = str(session['rand']) + ' is the number!!'
        session['color'] = 'green'
    elif session['rand'] > int(request.form['usernum']):
        session['result'] = 'Too low!'
        session['color'] = 'red'
    elif session['rand'] < int(request.form['usernum']):
        session['result'] = 'Too high!'
        session['color'] = 'red'
    
    print(session['result'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)