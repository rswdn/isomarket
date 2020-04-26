import flask
from flask import jsonify, request
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
        if self.confirmPassword == self.password:
           self.hashed =  bcrypt.hash(self.confirmPassword) #If passwords match, hashpassword
           #commiting all to the database & returning successful string
           c.execute("INSERT INTO users (username,password) VALUES(%s, %s)",(self.username,self.hashed))
           connection.commit()
           c.close()

        return('User successfully created') 


        





        


