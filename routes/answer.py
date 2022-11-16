from flask import Blueprint, render_template ,request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import certifi

answer = Blueprint("answer", __name__, url_prefix="/answer")

load_dotenv()
DB = os.getenv('DB')
client = MongoClient(DB, tlsCAFile=certifi.where())

db = client.testQuestions

@answer.route('/')
def answer_home():
    return render_template('answer.html')









# 서버 쪽에서 일단 게시글 제목 가져오기 ,
