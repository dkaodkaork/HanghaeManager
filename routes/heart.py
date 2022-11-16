from flask import Blueprint, render_template ,request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi
import jwt

SECRET_KEY = 'HANGHAE'


heart = Blueprint("heart", __name__, url_prefix="/heart")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.manager


@heart.route('/')
def heart_home():
    return render_template('index.html')

@heart.route('/update', methods=['POST'])
def update_heart():
    token_receive = request.cookies.get('mytoken')
    # db.testQuestions.update_one({'question_id':int(id_receive)},{'$set':{'q_heart_count':heart_num}})

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        quest_id = request.form['quest_id']
        userinfo = db.users.find_one({'user_id': payload['user_id']}, {'_id': 0})
        print(userinfo)
        q_heart = userinfo['q_heart_list'];
        print(q_heart)
        # try:
        #     # 중복 검사 실패
        #     quest_heart = db.users.find_one({'q_heart_list':quest_id})
        #     print('not none')
        # except:
        #     # 중복 검사 성공
        #     quest_heart = None
        # if quest_heart is None:
        #     db.users.update_one({'user_id':payload['user_id']},{'$push':{'q_heart_list':quest_id}})
        # else:
        #     overlap = "fail"


        return jsonify({'result': 'success', 'user_name': userinfo['user_name']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

