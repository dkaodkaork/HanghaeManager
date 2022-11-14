from flask import Blueprint, render_template

join = Blueprint("join", __name__, url_prefix="/join")

@join.route('/')
def join_home():
    return render_template('join.html')
