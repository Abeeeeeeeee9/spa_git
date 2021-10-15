from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbproject

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('review-layout.html')


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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)