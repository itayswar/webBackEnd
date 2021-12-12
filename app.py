from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

userNameVar = ''

@app.route('/home')
@app.route('/')
def index():
    return render_template('cv.html')


if __name__ == '__main__':
    app.run(debug=True)
