import flask
from flask import Flask, request, session
import pytest
from app import app
 

   
@pytest.fixture(scope='session', autouse=True)
def client():
    return app.test_client()
  
def test_addvalue(client):
    data ={"worker":"Marisee"}
    url = 'http://localhost:5000/addvalue'
    response = client.post(url, data=data)
    assert response.status_code == 200
