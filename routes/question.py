from flask import Blueprint, render_template

question = Blueprint("question", __name__, url_prefix="/question")

@question.route('/')
def question_home():
    return render_template('question.html')
