from flask import Flask, render_template, request, jsonify
from routes.join import join
from routes.login import login
from routes.main import main
from routes.mypage import mypage
from routes.question import question
from routes.answer import answer
from routes.post import post

app = Flask(__name__)


app.register_blueprint(join)
app.register_blueprint(login)
app.register_blueprint(main)
app.register_blueprint(mypage)
app.register_blueprint(question)
app.register_blueprint(answer)
app.register_blueprint(post)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)