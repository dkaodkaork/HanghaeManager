from flask import Blueprint, render_template

main = Blueprint("main", __name__, url_prefix="/bulletin-board")

@main.route('/')
def main_home():
    return render_template('main.html')
