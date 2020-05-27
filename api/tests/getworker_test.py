import flask
from flask import Flask, request
import pytest
from app import app
   
   
   
@pytest.fixture
def client():
    return app.test_client()
  
def test_worker(client):
    session['user'] == True
    data ={"worker":"Marisee"}
    url = 'http://localhost:5000/add'
    response = client.post(url, data=data)
    assert response.status_code == 200

def test_wrong_worker(client):
    data ={"worker":"Test"}
    url = 'http://localhost:5000/add'
    response = client.post(url, data=data)
    assert response.status_code == 401
