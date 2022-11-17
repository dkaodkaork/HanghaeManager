from flask import Blueprint, render_template ,request, url_for, jsonify, redirect
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi
from db import db

import routes.login as jwt_check
import routes.common_function as common_function

question = Blueprint("question", __name__, url_prefix="/question")

@question.route('/')
def question_home():
    return render_template('question.html')

@question.route("/question", methods=["POST"])
def question_post():

    user_check = jwt_check.user_check()

    if user_check['result'] != "fail":

        user_id = user_check['user_id']
        user = db.users.find_one({'user_id': user_id}, {'_id': False})
        user_name = user['user_name']

        question_title_receive = request.form['question_title_give']
        question_detail_receive = request.form['question_detail_give']
        main_ability_receive = request.form['main_ability_give']
        question_list = list(db.question.find({},{'_id': False}))
        count = len(question_list) +1
        question_date = common_function.now_time('othertime')


        doc = {
            'user_id': user_id,
            'user_name': user_name,
            'question_id': count,
            'answer_list': [],
            'q_heart_count': 0,
            'question_date': question_date,
            'question_detail': question_detail_receive,
            'main_ability': main_ability_receive,
            'question_title': question_title_receive,

        }

        db.question.insert_one(doc)

        return jsonify({"success": "success", "message": "게시글 등록 완료!"})

    else:
        return jsonify({"success": "fail", 'message': "다시 시도해주세요."})