from flask import Flask
app = Flask('talks')
app.config.from_object('talks_application.settings')
app.config.from_envvar('TALKS_SETTINGS')

import talks_application.actions
