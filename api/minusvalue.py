from flask import jsonify, request, abort, session
from db import connection

c = connection.cursor()
   
class minusValue:

    def __init__(self):
        self.newBalance = ''
        self.value_row = ''
        self.minusValue = ''
        self.worker = ''
  
  
    def updateMinusValue(self):
        self.worker = session.get('worker')
        self.value_row = session.get("value")
        self.minusValue = request.form['total'] #fetching the new result to be minused from the client
        self.newBalance = int(self.value_row) - int(self.minusValue) #adding the new value with th    e current balance to get the newBalance
        c.execute("UPDATE workers SET value = %s WHERE name = %s",(self.newBalance,self.worker))
        connection.commit()
        return jsonify(self.newBalance)
