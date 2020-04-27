import flask
from flask import jsonify, request
from db import connection

c = connection.cursor()

class workers:

    def __init__(self):
        self.name = ''
        self.value = ''

    def getWorker(self):
        c.execute('SELECT * FROM workers')
        rows = c.fetchall()

        return rows







   
