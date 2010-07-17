#coding:utf-8
from talks_application import app
from talks_application.models import *
from datetime import datetime

@app.route('/')
def index():
    return 'Hello world'
