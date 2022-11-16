from flask import Blueprint, render_template, request, jsonify

join = Blueprint("join", __name__, url_prefix="/join")

from db import db

import jwt

import datetime

import hashlib


@join.route('/')
def join_home():
    return render_template('join.html')


@join.route('/check', methods=['GET'])
def id_overlap_check():
    user_id = request.args.get('user_id')
    result = db.users.find_one({'user_id': user_id})
    print(result)
    if result == None:
        doc = {"message": "사용 가능한 아이디 입니다.", "success": True}
        return jsonify(doc)
    else:
        doc = {"message": "이미 사용중인 아이디 입니다.", "success": False}
        return jsonify(doc)


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
        'til_count': til_count,
        'q_heart_list': [],
        'a_heart_list': []
    }

    db.users.insert_one(doc)
    return jsonify({'result': 'success'})
