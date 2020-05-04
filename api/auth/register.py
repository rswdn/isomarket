import flask
from flask import jsonify, request, abort
from passlib.hash import bcrypt
from db import connection

c = connection.cursor()

class register:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.confirmPassword = ''
        self.hashed = ''

    def newUser(self):
        #getting username and password
        self.username = request.form['username']
        self.password = request.form['password']
        self.confirmPassword = request.form['confirmPassword']
        #checking if passwords match
        c.execute("SELECT username FROM users WHERE username = %s;",(self.username,))
        rows = c.fetchone()
        if rows is not None: #If username exists, retrun 401 error
            return abort(401, description='Username already taken, please try again. ')
        else: # if not username is not taken, check if passwords match
            if self.confirmPassword != self.password: #if not matched, retrun 401 error
                return abort(401, description='Passwords do not match, please try again. ')

            elif self.confirmPassword == self.password:
                self.hashed =  bcrypt.hash(self.confirmPassword) #If passwords match, hashpassword
                #commiting all to the database & returning successful string
                c.execute("INSERT INTO users (username,password) VALUES(%s, %s)",(self.username,self.hashed))
                connection.commit()
                c.close()

                return('User successfully created') 


        





        


