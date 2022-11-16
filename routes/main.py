from flask import Blueprint, render_template, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

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
        print(x['question_date'])
    return jsonify({'quests':quests_list})
    