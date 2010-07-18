import sys
import os

app_path = os.path.dirname(os.path.abspath(__file__)).replace('/tests/unit', '')

def setup():
    sys.path.append(app_path)
    from talks_application import app
    app.TESTING = True

def teardown():
    sys.path.remove(app_path)
