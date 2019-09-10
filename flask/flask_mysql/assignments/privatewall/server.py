from flask import Flask, render_template,redirect,request,session,flash
from db import connectToMySQL
from flask_bcrypt import Bcrypt
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secretkey'
bcrypt = Bcrypt(app)

################## ROOT ROUTE ####################
@app.route('/')
def root():
    return render_template('index.html')

################## LOGIN POST PROCESS ####################
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
            session['fname'] = result[0]['first_name']
            session['count'] = 0
            return redirect('/success')
    flash("Log in failed", "login-error")
    return redirect('/')

################### DASHBOARD #####################
@app.route('/success')
def success():
    if 'userid' in session:

        mysql = connectToMySQL('usersdbase')
        query = "SELECT * FROM users WHERE id=%(id)s"
        data = {
            'id': session['userid']
        }
        user = mysql.query_db(query, data)
        
        #############  RETRIEVE OTHER USERS ##############
        mysql = connectToMySQL('usersdbase')
        userquery = "SELECT * FROM users WHERE id !=%(id)s"
        users = mysql.query_db(userquery, data)

        ######### RETRIEVE MY MESSAGES #################
        mysql = connectToMySQL('usersdbase')
        messageQuery = "SELECT * FROM messages WHERE sent_to =%(id)s"
        messages = mysql.query_db(messageQuery, data)
        timenow = datetime.now(tz=None).hour
        countMessages = len(messages)
        return render_template('success.html', user=user, users=users, messages=messages, timenow=timenow, countMessages=countMessages)
    else:
        flash("You must be logged in to enter this website", "login-error")
        return redirect('/')

#################### REGISTER NEW USER #####################
@app.route("/register", methods=['POST'])
def register():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    print(session['fname'])
    isValid = True

    onlyLetters_REGEX = re.compile("^[a-zA-Z]+$")
    email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

############### GET EMAIL FOR VALIDATIONS #################
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
        session['fname'] = request.form['fname']
        flash("User successfully registered!", "reg-success")
        return redirect('/success')
    else:
        return redirect('/')

################# LOG OUT AND SESSION CLEAR ##################
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

################# SEND A MESSAGE POST PROCESS ##################
@app.route('/send-message', methods=['POST'])
def send():
    mysql = connectToMySQL('usersdbase')
    query = "INSERT INTO messages(sent_to, sent_by, message, created_at) VALUES(%(sent_to)s, %(sent_by)s, %(message)s, NOW())"
    data = {
        'sent_to': request.form['id'],
        'sent_by': session['fname'],
        'message': request.form['message']
    }
    
    mysql.query_db(query, data)
    flash("Message sent!","sent")
    session['count'] += 1
    return redirect('/success')

############### DELETE MESSAGE ROUTE ###################
@app.route('/message/<id>/delete/')
def message_delete(id):
    mysql = connectToMySQL('usersdbase')
    query = "DELETE FROM messages WHERE id="+id

    mysql.query_db(query)
    return redirect('/success')


if __name__=="__main__":
    app.run(debug=True)