#coding:utf-8
from talks_application import app
from talks_application.models import *

from google.appengine.api import users

from flask import redirect

@app.route('/')
def index():
    return 'Hello world'

@app.route('/login')
def redirect_to_login():
    return redirect(users.create_login_url('/'))

@app.route('/logout')
def redirect_to_logout():
    return redirect(users.create_logout_url('/'))
