from flask import Blueprint, render_template ,request, jsonify
import routes.common_function as common_function
from db import db
import routes.login as jwt_check

post = Blueprint("post", __name__, url_prefix="/post")

@post.route('/')
def post_home():
    return render_template('answer.html')


# 답변 저장 APi
@post.route('/answer', methods=['POST'])
def answer_insert():
    # try:

        user_check = jwt_check.user_check()

        if user_check['result'] != "fail":
            user_id = user_check['user_id']


            question_id = int(request.form['question_id'])
            answer_detail = request.form['answer_detail']

            user = db.users.find_one({'user_id': user_id}, {'_id': False})
            user_name = user['user_name']

            answer_date = common_function.now_time('othertime')

            # question_id일 때의 데이터 중 answer_list의 값 중 가장 최신일 때의 데이터
            question = db.question.find_one({'question_id': question_id}, {'answer_list': {'$slice': -1}})
            print(question)
            # 가장 최신의 answer_id를 가져옴

            if len(question['answer_list']) != 0:
                answer_id = question['answer_list'][0]['answer_id']
                answer_id = answer_id + 1
            else: answer_id = 1
        
            doc = {
                'user_id': user_id,
                'user_name': user_name,
                'answer_date': answer_date,
                'answer_id': answer_id,
                'answer_detail': answer_detail,
                'a_heart_count': 0
            }

            # question_id일 때의 answer_list 필드에  답변 추가
            db.question.update_one({'question_id': question_id}, {'$push': {'answer_list': doc}})

            return jsonify({"message": "댓글 등록 완료!"})
           

        else:
            return render_template('login.html')

    # except: return jsonify({"message": "다시 시도해주세요."})