from flask import Flask, render_template
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wedu'

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    


    return app
