# coding: utf-8
"""
Module containing templates filter for using in Jinja

Author: Francisco Souza
"""

def dateformat(value, fmt = '%m/%d/%Y'):
    """Formats a date object (datetime.date instance) to
    the specified output format"""
    return value.strftime(fmt)
