import flask 
from flask import request, jsonify, redirect, url_for
import test
from auth.register import register
from auth.login import login

app = flask.Flask(__name__)
app.config['DEBUG'] = True
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1><p>This is a test</p>"

@app.route('/test', methods=['GET'])
def books():
    return jsonify(test.books)

@app.route('/auth/register', methods=['POST', 'GET'])
def registerUser():
    result_register = register().newUser()
    return jsonify(result_register)

@app.route('/auth/login', methods=[ 'POST'])
def loginUser():
    result_login = login().userLogin()
    return jsonify(result_login)

app.run()
