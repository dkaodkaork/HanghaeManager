from flask import Blueprint, render_template

login = Blueprint("answer", __name__, url_prefix="/answer")

@login.route('/')
def login_home():
    return render_template('answer.html')
