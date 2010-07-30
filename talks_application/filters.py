# coding: utf-8
"""
Module containing template filters for using in Jinja

Author: Francisco Souza
"""
from talks_application import app

@app.template_filter('dateformat')
def dateformat(value, fmt = '%m/%d/%Y'):
    """Formats a date object (datetime.date instance) to
    the specified output format"""
    return value.strftime(fmt)
