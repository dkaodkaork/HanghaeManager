from flask import Blueprint, render_template ,request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

answer = Blueprint("answer", __name__, url_prefix="/answer")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.manager

@answer.route('/')
def answer_home():
    return render_template('answer.html')


@answer.route("/<question_id>", methods=["GET"])
def question_detail_get(question_id):
    print(question_id)
    question_list = list(db.question.find({'question_id': int(question_id)},{'_id':False}))
    print(( question_list))
    return jsonify({'question_list': question_list})






