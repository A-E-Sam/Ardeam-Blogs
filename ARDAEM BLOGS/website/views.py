from flask import Flask, render_template, Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html") 