from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['TODO 12', 'TODO 23', 'TODO 34']



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    }

    # **context: sirve para expandir las variables, en caso de no tener ** lo va a setear como diccionario
    return render_template('hello.html', **context)