import flask
from flask import Flask, request, session
import pytest
from app import app
 
   
@pytest.fixture
def client():
    return app.test_client()
 
#testing the minusing balance function
def test_minusvalue(client):
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess['user'] = True
            sess['value'] = '300'
            sess['worker'] = 'Marisee'
        data ={"total":"200",
              "value":sess['value'],
              "worker":sess['worker']}
        url = 'http://localhost:5000/minusvalue'
        response = c.post(url, data=data)
        assert response.status_code == 200
  
  #Sending a request without a total returning a 400
def test_missngvalue(client):
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess['user'] = True
            sess['value'] = '100'
            sess['worker'] = 'Marisee'
        data ={"value":sess['value'],
              "worker":sess['worker']}
        url = 'http://localhost:5000/minusvalue'
        response = c.post(url, data=data)
        assert response.status_code == 400
