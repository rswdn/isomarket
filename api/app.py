import flask 
from flask import request, jsonify, redirect, url_for
import test
from auth.register import login

app = flask.Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This is a test</p>"

@app.route('/test', methods=['GET'])
def books():
    return jsonify(test.books)

@app.route('/auth/register', methods=['POST', 'GET'])
def test():
    return jsonify(login.newUser())

app.run()
