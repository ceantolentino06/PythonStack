from flask import Flask, render_template, redirect, request
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

hashed = bcrypt.generate_password_hash('mypassword123')
print(bcrypt.check_password_hash(hashed, 'mypassword123'))

if __name__=="__main__":
    app.run(debug=True)