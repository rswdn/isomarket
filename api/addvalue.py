from flask import jsonify, request, abort, session
from db import connection
   
c = connection.cursor()
   
class addValue:
 
    def __init__(self):
        self.newBalance = ''
        self.value_row = ''
        self.addValue = ''
        self.worker = ''
  
  
    def updateValue(self):
        self.worker = session.get('worker')
        self.value_row = session.get("value")
        self.addValue = request.form['total'] #fetching the new result to be added from the client
        self.newBalance = int(self.value_row) + int(self.addValue) #adding the new value with the curren    t balance to get the newBalance
        c.execute("UPDATE workers SET value = %s WHERE name = %s;"(self.newBalance, self.worker,))
        conn.commit()
        conn.close()
  
        return jsonify(self.newBalance)
  

 
  

