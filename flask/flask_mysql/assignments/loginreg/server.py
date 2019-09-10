from flask import Flask, render_template,redirect,request,session,flash
from db import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secretkey'
bcrypt = Bcrypt(app)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('usersdbase')
    query = "SELECT * FROM users WHERE email=%(email)s"
    data = {
        'email': request.form['email']
    }
    result = mysql.query_db(query, data)
    print(result)
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['userid'] = result[0]['id']
            return redirect('/success')
    flash("Log in failed", "login-error")
    return redirect('/')

@app.route('/success')
def success():
    if 'userid' in session:
        mysql = connectToMySQL('usersdbase')
        query = "SELECT * FROM users WHERE id=%(id)s"
        data = {
            'id': session['userid']
        }
        user = mysql.query_db(query, data)
        return render_template('success.html', user=user)
    else:
        flash("You must be logged in to enter this website", "login-error")
        return redirect('/')

@app.route('/check-em', methods=['POST'])
def check_email():
    found = False
    mysql = connectToMySQL('usersdbase')
    query = "SELECT * FROM users WHERE email=%(email)s"
    data = {
        'email': request.form['email']
    }
    result = mysql.query_db(query,data)
    print(result)
    if result:
        found = True
    return render_template('partials/email.html', found=found)


@app.route("/register", methods=['POST'])
def register():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    isValid = True

    onlyLetters_REGEX = re.compile("^[a-zA-Z]+$")
    email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    mysql = connectToMySQL('usersdbase')
    query = "SELECT * FROM users WHERE email=%(email)s"
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query,data)

    if len(request.form['fname']) > 1:
        if not onlyLetters_REGEX.match(request.form['fname']):
            isValid = False
            flash("Name should only have letters", "fname")
    else:
        isValid = False
        flash("Fill this area", "fname")
    
    if len(request.form['lname']) > 1:
        if not onlyLetters_REGEX.match(request.form['lname']):
            isValid = False
            flash("Name should only have letters", "lname")
    else:
        isValid = False
        flash("Fill this area", "lname")
    
    if len(request.form['email']) > 1:
        if user:   
            isValid = False
            flash("This email is already registered", "email")   
        else:
            if not email_REGEX.match(request.form['email']):
                isValid = False
                flash("Email should be a valid email address", "email")
    else:
        isValid = False
        flash("Fill this area", "email")

    if len(request.form['password']) > 1:
        if len(request.form['password']) < 8:
            isValid = False
            flash("Password must 8 characters or more", "password")
    else:
        isValid = False
        flash("Fill this area", "password")
    
    if len(request.form['confpw']) > 1:
        if request.form['confpw'] != request.form['password']:
            isValid = False
            flash("Password does not match", "confpw")
    else:
        isValid = False
        flash("Fill this area", "confpw")
    

    if isValid:
        encrypt = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('usersdbase')
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW())"
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'password': encrypt
        }
        newUser = mysql.query_db(query, data)
        session.clear()
        session['userid'] = newUser
        flash("User successfully registered!", "reg-success")
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)