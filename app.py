from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

userNameVar = ''

@app.route('/')
def index():
    return render_template('cv.html')

@app.route('/assignment8')
def ass8():
    return render_template('hobbies.html', hobbies=['sport', 'movies', 'reading'])






if __name__ == '__main__':
    app.run(debug=True)
