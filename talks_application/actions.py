#coding:utf-8
from talks_application import app

@app.route('/')
def index():
    return 'Hello world'

@app.route('/hello/<nome>')
def ser_educado(nome):
    return 'Oi %s' %nome
