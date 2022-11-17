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

@heart.route('/question', methods=['POST'])
def update_Qheart():
    token_receive = request.cookies.get('mytoken')
    # db.testQuestions.update_one({'question_id':int(id_receive)},{'$set':{'q_heart_count':heart_num}})

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        quest_id = request.form['quest_id']
        userinfo = db.users.find_one({'user_id': payload['user_id']}, {'_id': 0})
        print(userinfo)
        q_heart_list = userinfo['q_heart_list'];
        result = quest_id in q_heart_list
        if not result :
            db.question.update_one({'question_id':int(quest_id)},{'$inc':{'q_heart_count':1}},True)
            db.users.update_one({'user_id': payload['user_id']},{'$push':{'q_heart_list':quest_id}})
            
        return jsonify({'result': 'success', 'user_name': userinfo['user_name'],'tf': result})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})



@heart.route('/answer', methods=['POST'])
def update_Aheart():
    token_receive = request.cookies.get('mytoken')
    # db.testQuestions.update_one({'question_id':int(id_receive)},{'$set':{'q_heart_count':heart_num}})

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        answer_id = request.form['answer_id']
        userinfo = db.users.find_one({'user_id': payload['user_id']}, {'_id': 0})
        print(userinfo)
        a_heart_list = userinfo['a_heart_list'];
        result = answer_id in a_heart_list
        print(result)
        # test = db.question.find_one({
        #     'question_id':8,
        #     "$elemMatch":{"answer_list":
        #     {"$elemMatch":{'answer_id':
        #     int(answer_id)}}}})
        
        # print(test)
        # test2 = test['answer_list']
        # for i in test2:
        #     if i['answer_id'] == int(answer_id):
        #         i['a_heart_count'] +=1
        # if not result :
            # db.question.update_one({'question_id':int(answer_id)},{'$inc':{'a_heart_count':1}},True)
            # db.users.update_one({'user_id': payload['user_id']},{'$push':{'q_heart_list':quest_id}})
            
        return jsonify({'result': 'success', 'user_name': userinfo['user_name'],'tf': result})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


