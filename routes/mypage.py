from flask import Blueprint, render_template

mypage = Blueprint("mypage", __name__, url_prefix="/mypage")


@mypage.route('/')
def mypage_home():
    return render_template('mypage.html')
