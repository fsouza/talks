#coding:utf-8
from talks_application import app
from talks_application.models import *
from datetime import datetime

from google.appengine.api import users

@app.route('/')
def index():
    return 'Hello world'

@app.route('/hello/<nome>')
def ser_educado(nome):
    t = Talk(
        title = nome,
        description = nome,
        date = datetime.today(),
        presented_by = users.get_current_user()
    )
    t.put()
    return '%s talk registered' %nome

@app.route('/talks')
def see_talks():
    talks = Talk.all()
    string = ''
    for talk in talks:
        string += talk.title
        string += '<br />'
    return string
