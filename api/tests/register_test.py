import flask
from flask import Flask, request
import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()


#def test_new_user(client):
 #   data ={"username":"test321", "password":"test321", "confirmPassword":"test321"}
  #  url = 'http://localhost:5000/auth/register'
   # response = client.get(url, data=data)
    #assert response.status_code == 200
def test_wrong_username(client):
    data ={"username":"test321", "password":"test321", "confirmPassword":"test321"}
    url = 'http://localhost:5000/auth/register'
    response = client.post(url, data=data)
    assert response.status_code == 401

def test_wrong_password(client):
    data ={"username":"test1245", "password":"test321", "confirmPassword":"test123"}
    url = 'http://localhost:5000/auth/register'
    response = client.post(url, data=data)
    assert response.status_code == 401
