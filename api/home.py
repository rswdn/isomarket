import flask
from flask import jsonify, request, session, abort
from db import connection

c = connection.cursor()

class workers:

    def __init__(self):
        self.name = ''
        self.value = ''
        self.worker = ''

    def displayWorker(self):
        c.execute('SELECT * FROM workers')
        rows = c.fetchall()
        
        return rows

    def getWorker(self):
          self.worker = request.form['worker']#getting the username
          c.execute("SELECT name FROM workers WHERE name = %s;", (self.worker,))#executing 
          rows = c.fetchone()#fetcing results
          #checking if user exists
          if rows is None: #if not return 401 error
              return abort(404)
          else:
              session['worker'] = request.form['worker']
              return jsonify('add.html')



   
