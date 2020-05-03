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
    
    

    def add(self):
        self.worker = request.form['worker_button']#getting the username
        c.execute("SELECT name FROM workers WHERE name = %s;", (self.worker,))#executing 
        row = c.fetchone#fetcing results
        
        #checking if user exists, then getting the current balance
        if row == self.worker:
            c.execute("SELECT value FROM workers WHERE name = %s;", (self.worker,))#Selecting the worker value based on the selectWOrker result
            value_row = c.fetchone()
            self.currentBalance = value_row #setting the currentBalance to the resut of the query
        # declearing all buttoms with values and fetching the reqult from the front end/client

            self.addValue = request.form['result'] #fetching the new result to be added from the client
            self.newBalance = int(self.currentBalance) + int(self.addValue) #adding the new value with the current balance to get the newBalance

            c.execute("UPDATE workers SET value = %s WHERE name = %s;"(self.newBalance, self.worker,))

            conn.commit()






        


            


            




