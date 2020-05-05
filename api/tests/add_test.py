import flask
from flask import Flask, request
import pytest
from app import app
 
@pytest.fixture
def client():
    return app.test_client()     

def test_getWorker(client):
    data = {"worker_button": "Marisee"}
    url = 'http://localhost5000:/add'
    response = client.post(url, data=data)
    assert response.status_code == 200

