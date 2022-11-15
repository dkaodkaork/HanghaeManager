
from flask import Blueprint, render_template, request, jsonify

join = Blueprint("join", __name__, url_prefix="/join")

from db import db

import jwt

import datetime

import hashlib



@join.route('/')
def join_home():
    return render_template('join.html')

# @join.route('/check', methods=['POST'])
# def id_overlap_check(request):
#     id_receive = request.form['id_give']
#     try:
#         # 중복 검사 실패
#         user = db.users.find_one(id_receive)
#     except:
#         # 중복 검사 성공
#         user = None
#     if user is None:
#         overlap = "pass"
#     else:
#         overlap = "fail"
#     return jsonify({'result': 'fail'})


# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@join.route('/join', methods=['POST'])
def api_join():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    til_count = 0

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'user_id': id_receive,
        'user_pw': pw_hash,
        'user_name': name_receive,
        'til_count': til_count
    }


    db.user.insert_one(doc)
    return jsonify({'result': 'success'})
