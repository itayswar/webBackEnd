from flask import Flask, redirect, url_for, request
from flask import render_template , session
app = Flask(__name__)

users  = ['Itay', 'Yossi', 'Dana', 'Mor', 'Yuval']
app.secret_key = '123'

@app.route('/')
def index():
    return render_template('cv.html')

@app.route('/assignment8')
def ass8():
    return render_template('hobbies.html',
                           hobbies=['sport', 'hunting', 'reading'],
                           movies=['matrix', 'harry potter', 'die hard'])

@app.route('/assignment9', methods = ['POST' ,'GET'])
def ass9():
    currMethod = request.method
    if currMethod == 'GET':
        if 'name' in request.args:
            if request.args['name']=='':
                messege = users
            else:
                if request.args['name'] in users:
                        messege = request.args['name'] + ' is in the list !'
                else:
                    messege = request.args['name'] + ' is not registered !'
        else:
            messege = 'first'
    if currMethod == 'POST':
        if session['name']:
            session['name'] = ''
        else:
            session['name'] = request.form['name']
        messege = 'first'


    return render_template('assignment9.html',
                           messege = messege,
                           currMethod = currMethod
                           )

if __name__ == '__main__':
    app.run(debug=True)

