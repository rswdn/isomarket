import flask
from flask import Flask, request
import pytest
from app import app
 
@pytest.fixture
def client():
    return app.test_client()     

def test_addValue(client):
    worker = {"worker_button": "Marisee"}
    url = 
