import flask
from flask import jsonify, request
from db import connection

c = connection.cursor()

class workers:

    def __init__(self):
        self.name1 = ''
        self.value1 = ''

        self.name2 = ''
        self.value2 = ''

        self.name3 = ''
        self.value3 = ''

    def getWorker(self):
        c.execute('SELECT * FROM workers')
        rows = c.fetchall()

        self.name1 = rows[1:1]
        self.value1 = [2]


        self.name2 = rows[1]
        self.value2 = rows[2]
        
        self.name3 = [1]
        self.value3 = [2]

        print(self.name1)








   
workers().getWorker()
