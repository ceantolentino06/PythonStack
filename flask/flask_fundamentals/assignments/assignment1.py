from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/<value>')          # The "@" decorator associates this route with the function immediately following
def hello_world(value):
    return f'Hello {value}'

@app.route('/say/<name>')
def say_hello(name):
    return f'Hi {str(name)}!'

@app.route('/repeat/<times>/<value>')
def repeat(times, value):
    return str(value)*int(times)
if(__name__ == "__main__"):
    app.run(debug=True)