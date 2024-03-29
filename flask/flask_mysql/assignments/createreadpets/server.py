from flask import Flask, render_template, redirect, request
from db import connectToMySQL

app = Flask(__name__)
@app.route('/')
def root():
    mysql = connectToMySQL('petsdb')
    pets = mysql.query_db("SELECT * FROM pets")
    return render_template('index.html', pets = pets)

@app.route('/add_pet', methods=['POST'])
def add_pet():
    mysql = connectToMySQL('petsdb')
    query = "INSERT INTO pets(name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        'name': request.form['name'],
        'type': request.form['type']
    }
    newPet = mysql.query_db(query, data)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)