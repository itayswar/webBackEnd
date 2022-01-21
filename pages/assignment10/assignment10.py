from flask import Flask, redirect, url_for, request, Blueprint
from flask import render_template , session
import mysql.connector
import mysql
import mysql.connector
import requests
from flask import Flask, render_template, session, request, redirect, Blueprint, Response
import json



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


# about blueprint definition
assignment10 = Blueprint(
                  'assignment10',
                  __name__,
                  static_folder='static',
                  static_url_path='/assignment10',
                  template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def ass10():
    currMethod = request.method
    messege=''
    return render_template('assignment10.html',
                           messege = messege,
                           currMethod = currMethod)

@assignment10.route('/insert_user', methods = ['GET', 'POST'])
def insert_user():
    currMethod = request.method
    messege = ''
    name = request.form['nameIns']
    if name:
        messege = 'user inserted!'
        query = "insert into users(name) values ('%s')" % (name)
        interact_db(query = query, query_type='commit')
    return render_template('assignment10.html',
                           messege = messege,
                           currMethod = currMethod)

@assignment10.route('/update_user', methods = ['GET', 'POST'])
def update_user():
    currMethod = request.method
    messege = ''
    nameOld = request.form['nameOld']
    nameNew = request.form['nameNew']
    if nameNew:
        messege = 'user updated!'
        query = "insert into users(name) values ('%s')" % (nameNew)
        interact_db(query = query, query_type='commit')
        query = "delete from users where name=('%s')" % (nameOld)
        interact_db(query = query, query_type='commit')
    return render_template('assignment10.html',
                           messege = messege,
                           currMethod = currMethod)

@assignment10.route('/delete_user', methods = ['GET', 'POST'])
def delete_user():
    currMethod = request.method
    messege = ''
    nameDlt = request.form['nameDlt']
    if nameDlt:
        messege = 'user deleted!'
        query = "delete from users where name=('%s')" % (nameDlt)
        interact_db(query = query, query_type='commit')
    return render_template('assignment10.html',
                           messege = messege,
                           currMethod = currMethod)

@assignment10.route('/get_user')
def get_user():
    currMethod = request.method
    messege=''
    query = "select * from users"
    messegeTemp = interact_db(query = query, query_type='fetch')
    for user in messegeTemp:
        messege = messege + user.name + " "
    return render_template('assignment10.html',
                           messege = messege,
                           currMethod = currMethod)

@assignment10.route('/assignment12/restapi_users', defaults={'user_name': 'itay'})
@assignment10.route('/assignment12/restapi_users/<int:user_id>')
def get_user_data(user_name):
    query = f'''
    SELECT * from users WHERE user_name={user_name}
    '''
    user_data = interact_db(query=query, query_type='fetch', named_tuple=None, dictionary=True)
    if not user_data:
        user_data = {'error': f'user with name {user_name} was not found'}
    return Response(json.dumps(user_data), mimetype='application/json')


