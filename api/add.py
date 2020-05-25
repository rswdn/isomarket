import flask
from flask import jsonify, request, abort
from db import connection

c = connection.cursor()

class addMoney:

    def __init__(self):
        self.currentBalance = ''
        self.addValue = ''
        self.newBalance = ''
        self.worker = ''
        self.values = ''
    
    def getWorker(self):
        self.worker = request.form['worker']#getting the username
        c.execute("SELECT name FROM workers WHERE name = %s;", (self.worker,))#executing 
        rows = c.fetchone()#fetcing results
        #checking if user exists
        if rows is None: #if not return 401 error
            return abort(401, description='Something went wrong, please try again. ')
        else:
            return('Worked')
            #return(addMoney().add_value())

    def add_value(self):
        self.worker = self.worker
        c.execute("SELECT value FROM workers WHERE name = %s;", (self.worker,))#Selecting th        e worker value based on the selectWOrker result
        value_row = c.fetchone()
        self.currentBalance = value_row #setting the currentBalance to the resut of the query
        self.addValue = request.form['result'] #fetching the new result to be added from the client
        self.newBalance = int(self.currentBalance) + int(self.addValue) #adding the new value with the current balance to get the newBalance
        c.execute("UPDATE workers SET value = %s WHERE name = %s;"(self.newBalance, self.worker,))
        conn.commit()
        conn.close()

        return 







        


            


            




