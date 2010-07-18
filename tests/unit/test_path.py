from nose.tools import *
import os
import sys

def test_path():
    "Application root should be in PYTHONPATH"
    my_path = os.path.dirname(os.path.abspath(__file__))
    app_path = my_path.replace('/tests/unit', '')
    assert app_path in sys.path

def test_import_app():
    "Should import the app"
    try:
        from talks_application import app
    except ImportError:
        raise AssertionError('I can\'t import the app!')
