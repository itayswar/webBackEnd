from flask import Flask, redirect, url_for, request
from flask import render_template, session, blueprints
import mysql.connector
import json
import requests


app = Flask(__name__)
users  = ['Itay', 'Yossi', 'Dana', 'Mor', 'Yuval']
app.secret_key = '123'


def getUsers(index):
    ret = requests.get(f'https://reqres.in/api/users/{index}')
    return ret.json()


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='itay3636',
                                         database='ass_10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------------------------- #
# ------------------------------------------------- #

# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
## assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


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

@app.route('/assignment11')
def ass11():
    return render_template('assignment11.html', ind="ind", list='')


@app.route('/assignment11/users', methods = ['POST', 'GET'])
def ass11_users():
    dic = {}
    for user in interact_db(query="SELECT * FROM ass_10.users;", query_type='fetch'):
        dic[f'user_{user.name}'] = {
            'name': user.name
        }
    return render_template('assignment11.html', list=dic, ind="ind")

@app.route('/assignment11/outer_source',  methods=['post'])
def outerSource():
    if "front" in request.form:
        num = int(request.form['front'])
        return render_template('assignment11.html', front=num)
    elif "back" in request.form:
        num = int(request.form["back"])
        user = getUsers(num)
        return render_template('assignment11.html', back=user)
    else:
        return render_template('assignment11.html')




if __name__ == '__main__':
    app.run(debug=True)

