#coding:utf-8
from talks_application import app
from talks_application.models import *
from talks_application.forms import *
from talks_application.decorators import login_required

from google.appengine.api import users

from flask import redirect
from flask import render_template

@app.route('/')
def index():
    return 'Hello world'

@app.route('/login')
def redirect_to_login():
    return redirect(users.create_login_url('/'))

@app.route('/logout')
def redirect_to_logout():
    return redirect(users.create_logout_url('/'))

@app.route('/talks/new', methods=['GET'])
@login_required
def new_talk():
    form = TalkForm()
    return render_template('/talks/new.html', form=form)
