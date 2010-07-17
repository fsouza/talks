#!/usr/bin/python
from google.appengine.ext.webapp.util import run_wsgi_app
from talks_application import app

run_wsgi_app(app)
