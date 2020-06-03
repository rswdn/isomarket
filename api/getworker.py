import flask
from flask import jsonify, request, abort, session
from db import connection

c = connection.cursor()

class workerInfo:

    def __init__(self):
        self.currentBalance = ''
        self.addValue = ''
        self.newBalance = ''
        self.worker = ''
        self.values = ''
        
    
    def getWorker(self):
        self.worker = session.get("worker")
        c.execute("SELECT name,value FROM workers WHERE name = %s;", (self.worker ,))#Selecting the worker value based on the selectWorker result
        value_row = c.fetchone()

        if value_row is None: #if not return 401 error
            return abort(404, jsonify('Something went wrong'))
        else:
            session['value'] = value_row[1]
            return jsonify(value_row)







        


            


            



