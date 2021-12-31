from flask import Flask, redirect, url_for, request, Blueprint
from flask import render_template , session
import mysql.connector


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


