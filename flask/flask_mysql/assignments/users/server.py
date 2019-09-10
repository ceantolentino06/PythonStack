from flask import Flask, render_template, redirect, request
from db import connectToMySQL

app = Flask(__name__)
@app.route('/')
def root():
    mysql = connectToMySQL('usersdb')
    users = mysql.query_db("SELECT * FROM users")

    return render_template('index.html', users=users)

@app.route('/add_user')
def add_user():
    return render_template('/add.html')

@app.route('/add_process', methods=['POST'])
def add_process():
    mysql = connectToMySQL('usersdb')
    query = "INSERT INTO users (fullname, email, description, created_at, updated_at) VALUES(%(name)s, %(email)s, %(desc)s, NOW(), NOW());"
    data = {
        'name': request.form['fname'] + ' ' + request.form['lname'],
        'email': request.form['email'],
        'desc': request.form['desc']
    }

    newUser = mysql.query_db(query, data)
    print('**************************************',newUser)
    return redirect('/show_user/'+ str(newUser))

@app.route('/show_user/<id>')
def show_user(id):
    mysql = connectToMySQL('usersdb')
    user = mysql.query_db("SELECT * FROM users WHERE id="+id)
    print(user)
    print(id)
    return render_template('show.html', user=user)

@app.route('/edit_user/<id>')
def edit_user(id):
    mysql = connectToMySQL('usersdb')
    user = mysql.query_db("SELECT * FROM users WHERE id="+id)
    fullname = user[0]['fullname'].split()
    print(user[0])
    return render_template('edit.html', user=user, fullname=fullname)

@app.route('/edit_process', methods=['POST'])
def edit_process():
    mysql = connectToMySQL('usersdb')
    query = "UPDATE users SET fullname=%(name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s"
    data = {
        'name': request.form['fname'] + ' ' + request.form['lname'],
        'email': request.form['email'],
        'id': request.form['id']
    }
    mysql.query_db(query, data)
    return redirect('/show_user/'+str(request.form['id']))

@app.route('/delete_user/<id>')
def delete_user(id):
    mysql = connectToMySQL('usersdb')
    query = "DELETE FROM users WHERE id="+id
    mysql.query_db(query)
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)