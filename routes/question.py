from flask import Blueprint, render_template ,request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

question = Blueprint("question", __name__, url_prefix="/question")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.testQuestions

@question.route('/')
def question_home():
    return render_template('question.html')

@question.route("/question", methods=["POST"])
def question_post():
    question_title_receive = request.form['question_title_give']
    question_detail_receive = request.form['question_detail_give']
    main_ability_receive = request.form['main_ability_give']
    
    question_list = list(db.testQuestions.find({},{'_id':False}))
    count = len(question_list) +1
    
    doc = {
        'question_title': question_title_receive,
        'question_detail': question_detail_receive,
        'main_ability': main_ability_receive,
        'question_id': count
    }
    
    db.testQuestions.insert_one(doc)
    return 

