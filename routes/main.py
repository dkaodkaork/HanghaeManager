from flask import Blueprint, render_template, jsonify, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi
import jwt

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

main = Blueprint("main", __name__, url_prefix="/bulletin-board")

DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.manager

@main.route('/')
def main_home():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.users.find_one({'user_id': payload['user_id']}, {'_id': 0})

        # return jsonify({'result': 'success', 'username': userinfo['user_name']})
        return render_template('main.html', username = userinfo['user_name'])
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return render_template('main.html')
    except jwt.exceptions.DecodeError:
        return render_template('main.html')



@main.route("/rank", methods=["GET"])
def main_rank_get():
    count_list = list(db.users.find({}, {'_id': False}))
    rank_list = sorted(count_list, key= lambda x : x['til_count'], reverse=True)
    return jsonify({'ranks':rank_list[:5]})

@main.route("/questions", methods=["GET"])
def main_questions_get():
    quests_list = list(db.question.find({}, {'_id': False}))
    # rank_list = sorted(count_list, key= lambda x : x['til_count'], reverse=True)
    date = []
    for x in quests_list:
        # date = x['question_date'].strftime('%Y/%m/%d')
        x['question_date'] = str(x['question_date']).split(' ')[0]
    return jsonify({'quests':quests_list})
    