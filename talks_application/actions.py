#coding:utf-8
from talks_application import app
from talks_application.models import *
from talks_application.forms import *
from talks_application.decorators import login_required

from google.appengine.api import users

from flask import redirect, render_template, flash, url_for

from datetime import datetime

@app.route('/')
def index():
    talks = Talk.all().order('-date');
    return render_template('/talks/index.html', talks=talks)

@app.route('/logout')
def redirect_to_logout():
    return redirect(users.create_logout_url('/'))

@app.route('/talks/new', methods=['GET'])
@login_required
def new_talk():
    form = TalkForm()
    return render_template('/talks/new.html', form=form)

@app.route('/talks', methods=['POST'])
@login_required
def create_talk():
    form = TalkForm()
    if form.validate_on_submit():
        talk = Talk(
            title = form.title.data,
            date = form.date.data,
            description = form.description.data,
            presented_by = users.User()
        )
        talk.put()
        flash('Talk saved in the database')
        return redirect(url_for('index'))
    return render_template('/talks/new.html', form=form)
