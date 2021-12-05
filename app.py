from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'this is home!'

@app.route('/home')
def home():
    return redirect('/')

@app.route('/urlForEx')
def ex():
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
