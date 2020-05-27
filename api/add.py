import flask
from flask import jsonify, request, abort, session
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
        self.worker = session.get("worker")
        c.execute("SELECT name,value FROM workers WHERE name = %s;", (self.worker ,))#Selecting th        e worker value based on the selectWOrker result
        value_row = c.fetchone()

        if value_row is None: #if not return 401 error
            return abort(404, jsonify('Something went wrong'))
        else:
            return jsonify(value_row)

       # self.currentBalance = value_row #setting the currentBalance to the resut of the query
        #self.addValue = request.form['result'] #fetching the new result to be added from the client
        #self.newBalance = int(self.currentBalance) + int(self.addValue) #adding the new value with the current balance to get the newBalance
        #c.execute("UPDATE workers SET value = %s WHERE name = %s;"(self.newBalance, self.worker,))
        #conn.commit()
        #conn.close()

        #return 







        


            


            




