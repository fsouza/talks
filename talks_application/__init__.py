from flask import Flask
import settings

app = Flask('talks')
app.config.from_object('talks_application.settings')

import actions
import filters
