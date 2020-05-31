import flask 
from flask import request, jsonify, redirect, url_for, session, abort
from home import workers
from auth.register import register
from auth.login import login
from functools import wraps
from add import addMoney
from addvalue import addValue
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.secret_key = "super_secret_key"
CORS(app, supports_credentials=True)

@app.route('/auth/register', methods=['POST'])
def registerUser():
    result_register = register().newUser()
    return jsonify(result_register)

@app.route('/auth/login', methods=[ 'POST'])
def loginUser():
    response = login().userLogin()
    return response

@app.route('/logout', methods=['GET','POST'])
def logOut():
    if 'user' in session:
        session.pop('user', None)
        return "logged out"


@app.route('/add', methods=['POST'])
def get_worker():
    if 'user' not in session:
        return abort(401, description="You need to login!")
    else:
       response = addMoney().add()
       return response

@app.route('/addvalue', methods=['POST'])
def add_value(): 
    if 'user' not in session:
        return abort(401, description="You need to login!")
    else:
       response = addValue().updateValue()
       return response

@app.route('/home', methods=['GET', 'POST'])
def listWorker():
    if 'user' not in session:
        return abort(401, description="You need to login!")
    elif request.method == 'GET':
        response = jsonify(workers().displayWorker())
        return response
    else:
        response = workers().getWorker()
        return response

if __name__ == '__main__':
    app.run(debug=True)
