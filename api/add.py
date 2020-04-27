import flask
from flask import jsonify, request
from db import connection

c = connection.cursor()

class addMoney:

    def __init__(self):
        self.currentBalance = ''
        self.addValue = ''
        self.newBalance = ''
        self.worker = ''
        self.values = ''

    def selectWorker(self):
        self.worker = request.form['worker_button']#getting the username
        c.execute("SELECT name FROM workers WHERE name = %s;", (self.worker,))#executing 
        row = c.fetchone#fetcing results
        
        #checking if user exists, then getting the current balance
        if row == self.worker:
            addValue()

    def add(self):
        c.execute("SELECT value FROM workers WHERE name = %s;", (self.worker,))#Selecting the worker value based on the selectWOrker result
        value_row = c.fetchone()
        self.currentBalance = value_row #setting the currentBalance to the resut of the query

        self.values = request.form['value_button']
        self.addValue = []

        for value in self.values:
            self.addValue += self.values

            return[self.addValue]




        


            


            




