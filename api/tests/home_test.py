import flask
from flask import Flask, request, session
import pytest
from app import app
   
   
   
@pytest.fixture
def client():
    return app.test_client()
  
def test_notLoggedIn(client):
    url = 'http://localhost:5000/home'
    response = client.get(url)
    assert response.status_code == 401

def test_getUsers(client):
    session['logged_in'] = True
    url = 'http://localhost:5000/home'
    response = client.get(url)
    assert response.status_code == 200
