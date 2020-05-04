import flask
from flask import Flask, request
import pytest
from app import app



@pytest.fixture
def client():
    return app.test_client()

def test_login(client):
    data ={"username":"test8", "password":"test8"}
    url = 'http://localhost:5000/auth/login'
    response = client.post(url, data=data)
    assert response.status_code == 200


def test_login_error(client):
    data ={"username":"test900000", "password":"test9000"}
    url = 'http://localhost:5000/auth/login'
    response = client.post(url, data=data)
    assert response.status_code == 401
