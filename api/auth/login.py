import flask
from flask import jsonify, request, abort, json
from passlib.hash import bcrypt
from db import connection

c = connection.cursor()

class login:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.details = ''

    def userLogin(self):

        #getting username and password
        self.username = request.form.get('username')
        self.password = request.form.get('password')
        #pulling records from the database based on username
        c.execute("SELECT * FROM users WHERE username = %s;", (self.username,))
        rows = c.fetchone() #fetching the vaild row
        #checking if username exists, if not returing a 401 error 
        if rows is None:
           return abort(401, description='Incorrect username or password, please try again. ')
        #chcking if the username matches the inputted username
        elif rows[1] == self.username:
           result = bcrypt.verify(self.password, rows[2]) #using bcrypt to verify password

           return(result) # returing results 



#TODO adding a test to see if password matches, if not return 401 error and "incorect username or passowrd, please try again
# TODO redirect this to the vailid endpoint












        



