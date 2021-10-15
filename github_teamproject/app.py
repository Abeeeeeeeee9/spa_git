import flask
from flask import Flask, render_template, jsonify, request,redirect,url_for
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import xmltodict
import sys
import jwt
import datetime
import hashlib
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta





app = Flask(__name__)

SECRET_KEY = 'SPARTA'

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")
db = client.dbproject

@app.route('/')
def index():
    return render_template('1page2-.html')
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('1page2-.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))






@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60*60*24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# 로그인 페이지
@app.route('/login', methods=['GET'])
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


# 회원가입
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호

        "profile_pic": "",                                          # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


# 아이디 중복확인
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# 마이페이지
@app.route('/mypage', methods=['GET'])
def mypage():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('mypage.html', user_info=user_info)

    except (jwt.exceptions.DecodeError,jwt.ExpiredSignatureError):
        return redirect(url_for("/"))






#지역별 명소 데이터 api 가져오기
@app.route('/place',methods=['GET','POST'])
def show_place():

    #선택한지역 넘겨주기
    if request.method == 'POST':
        want = request.form.get('inputGroupSelect04')
        #print(want)
        places = db.sample.find({"area": want}, {'_id': False})

        places=list(places)

        return render_template('2page.html',data=want,places=places)

#명소의 자세한 페이지
@app.route('/detail',methods=['POST','GET'])
def show_detail():
    name = request.form['name_give']
    print(name)
    places = db.sample.find({"name": name}, {'_id': False})

    places = list(places)
    print(places)
    return {'result': places}


@app.route('/3page',methods=['GET'])
def show_detail2():
     name = request.args.get('name')
     places = db.sample.find({"name": name}, {'_id': False})
     places=list(places)
     print(places)
     return render_template('3page.html',place=places)

#공공데이터 api query url 만드는함수
def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

@app.route('/time',methods=['GET'])
def show_time():
    URL="http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService"
    OPERATION = 'getLCRiseSetInfo'
    SERVICEKEY="/oZ4AFQEH6WdKfRkiTxU9cNH8VHjxNsZO3PeRFfdDwIQLI3TfmMbjfQvhRSJyrACs3w1ARppFgEkiz5ebTfibg=="


    longitude = request.args.get('long',int)
    latitude = request.args.get('lati',int)
    date = request.args.get('date',int)
    PARAMS={
        'locdate':date,
        'longitude':longitude,
        'latitude':latitude,
        'dnYn':'y'

    }


    #response=requests.get("http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getLCRiseSetInfo?&longitude=" + longitude + "&latitude=" + latitude + "&locdate=" + date + "&dnYn=y&ServiceKey=/oZ4AFQEH6WdKfRkiTxU9cNH8VHjxNsZO3PeRFfdDwIQLI3TfmMbjfQvhRSJyrACs3w1ARppFgEkiz5ebTfibg==")
    request_query = get_request_query(URL, OPERATION, PARAMS, SERVICEKEY)

    response = requests.get(url=request_query)
    return response.text

## API 역할을 하는 부분
@app.route('/reviewpage', methods=['POST'])
def write_review():
    where_receive = request.form['where_give']
    upload_receive = request.form['upload_give']
    review_receive = request.form['review_give']

    doc = {
        'where':where_receive,
        'upload':upload_receive,
        'review':review_receive
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


@app.route('/reviewpage', methods=['GET'])
def read_reviews():
    go_reviews = list(db.reviews.find({}, {'_id': False}))

    return jsonify({'all_reviews': go_reviews})






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)