from flask import Flask, render_template, request
from multiselectfield import MultiSelectField

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show():
    print(request.form)
    arr = request.form.getlist('test')
    print(arr[0])
    return render_template('show.html', result=request.form, skills=arr)
if __name__ == "__main__":
    app.run(debug=True)