from flask import Blueprint, render_template, jsonify, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi
import jwt

SECRET_KEY = 'HANGHAE'

main = Blueprint("main", __name__, url_prefix="/bulletin-board")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.testManager

@main.route('/')
def main_home():
    return render_template('main.html')

@main.route("/rank", methods=["GET"])
def main_rank_get():
    count_list = list(db.testUsers.find({}, {'_id': False}))
    rank_list = sorted(count_list, key= lambda x : x['til_count'], reverse=True)
    return jsonify({'ranks':rank_list[:5]})

@main.route("/questions", methods=["GET"])
def main_questions_get():
    quests_list = list(db.testQuestions.find({}, {'_id': False}))
    # rank_list = sorted(count_list, key= lambda x : x['til_count'], reverse=True)
    date = []
    for x in quests_list:
        # date = x['question_date'].strftime('%Y/%m/%d')
        x['question_date'] = str(x['question_date']).split(' ')[0]
    return jsonify({'quests':quests_list})
    

@main.route('/name', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        userinfo = db.user.find_one({'user_id': payload['user_id']}, {'_id': 0})
        return jsonify({'result': 'success', 'user_name': userinfo['user_name']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
