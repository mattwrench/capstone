# Provides login and logout functions
import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

DEFAULT_USER = 'user'
DEFAULT_PASS = 'wgu'
# Hash the password for additional security
DEFAULT_PASS = generate_password_hash(DEFAULT_PASS)

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        # Extract information from HTTP request
        username = request.form['username']
        password = request.form['password']

        # Unsuccessful login
        if username != DEFAULT_USER:
            error = 'Invalid username'
        elif not check_password_hash(DEFAULT_PASS, password):
            error = 'Invalid password'

        # Successful login
        if error is None:
            session.clear()
            session['authenticated'] = True
            return redirect('/')
        
        flash(error)
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
        