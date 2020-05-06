import flask 
from flask import request, jsonify, redirect, url_for
from home import workers
from auth.register import register
from auth.login import login
from functools import wraps
from add import addMoney


app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def login_required(f):
    @wraps
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login")
            return redirect(url_for('login'))
    return wrap

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

@app.route('/add', methods=['GET','POST'])
def get_worker():
    result_add = addMoney().getWorker()
    return jsonify(result_add)

@app.route('/home', methods=['GET'])
def listWorker():
    result_worker = workers().getWorker()
    return jsonify(result_worker)
if __name__ == '__main__':
    app.run()
