from flask import Blueprint, render_template, request, jsonify

from db import db

import routes.common_function as common_function

mypage = Blueprint("mypage", __name__, url_prefix="/mypage")


# 마이 페이지 기본 정보 get
@mypage.route('/')
def mypage_home():

    user_id = "qwer"
    user = db.users.find_one({'user_id': user_id}, {'_id': False})

    return render_template('mypage.html', user_name=user['user_name'], til_count=user['til_count'])


# 내가 작성했던 리스트 get
@mypage.route('/data')
def mypage_data():
    user_id = "qwer"
    question_list = list(db.question.find({'user_id': user_id}, {'_id': False}))
    print(question_list)

    return jsonify({'question_list': question_list}), 200


# til 카운터 +1
@mypage.route('/til/keeping', methods=['POST'])
def mypage_til_save():
    user_id = "mina"

    til_url = request.form['til_url']
    print(til_url)
    til_count = request.form['til_count']
    print(til_count)
    date = common_function.now_time('sametime')

    db.users.update_one({'user_id': user_id}, {'$set': {'til_count': int(til_count) + 10}})
    doc = {
        'user_id': user_id,
        'til_url': til_url,
        'til_date': date
    }
    db.til.insert_one(doc)

    return jsonify({"message": "축하드려요 🎉 + 10 점을 획득하셨습니다! "}), 200


# 게시글 수정
@mypage.route('/modification', methods=['POST'])
def post_update():
    user_id = "qwer"

    question_id = request.form['question_id']
    question_detail = request.form['question_detail']

    # user_id와 question_id에 저장된 user_id가 맞는지 확인 하기 위한 find
    post = db.question.find_one({'question_id': question_id}, {'_id': False})

    # 같다면 update
    if post['user_id'] == user_id:
        db.question.update_one({'question_id': int(question_id)}, {'$set': {'question_detail': question_detail}})
        return jsonify({"message": "success"}), 200
    else:
        # 같지 않다면 fail
        return jsonify({"message": "fail"}), 203


# 게시글 삭제
@mypage.route('/deletion', methods=['POST'])
def post_delete():

    user_id = "qwer"

    question_id = request.form['question_id']

    # user_id와 question_id에 저장된 user_id가 맞는지 확인 하기 위한 find
    post = db.question.find_one({'question_id': question_id}, {'_id': False})
    print(post)
    # 같다면 delete
    if post['user_id'] == user_id:
        db.users.delete_one({'question_id': int(question_id)})
        # question의 answer들도 삭제하는 로직 추가 구현 필요
        return jsonify({"message": "success"}), 200
    else:
        # 같지 않다면 fail
        return jsonify({"message": "fail"}), 203
