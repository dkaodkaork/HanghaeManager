from flask import Blueprint, render_template ,request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi
import datetime
from datetime import date, timedelta

answer = Blueprint("answer", __name__, url_prefix="/answer")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.manager



@answer.route("/<question_id>")
def answer_home(question_id):
    
    # question_id = 8
    question_list = db.question.find_one({'question_id': int(question_id)}, {'_id':False})
    
    return render_template('answer.html' , question_list= question_list)




@answer.route("/")
def question_detail_get():

    # question_id = 8
    question_id = request.args.get('question_id')
    question_list = db.question.find_one({'question_id': int(question_id)},{'_id':False})
    print(question_list)
    
    return jsonify({'question_list': question_list})

