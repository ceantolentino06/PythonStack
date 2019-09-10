from flask import Flask, render_template

app = Flask(__name__)
@app.route('/<num>/<color>')
def root(num,color):
    return render_template('index.html',num=int(num),bgcolor=color)

if(__name__=="__main__"):
    app.run(debug=True)