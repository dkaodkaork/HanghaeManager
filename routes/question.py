from flask import Blueprint, render_template

question = Blueprint("question", __name__, url_prefix="/question")

@question.route('/')
def question_home():
    return render_template('question.html')




@question.route("/question", methods=["POST"])
def question_post():
    question_title_receive = request.form['question_title_give']
    question_detail_receive = request.form['question_detail_give']
    main_ability_receive = request.form['main_ability_give']
    # question_date_receive = request.form['question_date_give']
    # question_id_receive = request.form['question_id_give']

    doc = {
        'question_title': question_title_receive,
        'question_detail': question_detail_receive,
        'main_ability': main_ability_receive,
        # 'question_id': question_id_receive,
        # 'question_date' : question_date_receive
    }

    db.question.insert_one(doc)

    return jsonify({'msg': '질문 작성 완료!'})

   