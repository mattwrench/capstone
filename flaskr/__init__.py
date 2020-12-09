import os
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import functools
from werkzeug.security import check_password_hash, generate_password_hash

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '4tOXdR9*jLN),l&pkcf>4jGw}IU&Ld'

    # Index route
    # If user is not logged in, redirect to /login
    # If user is logged in, redirect to /dashboard
    @app.route('/')
    def index():
        if "authenticated" not in session:
            return redirect('/login')
        return redirect('/dashboard')

    # Load app blueprints
    from. import forecast
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import dash
    app.register_blueprint(dash.bp)

    return app