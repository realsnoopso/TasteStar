# flask setting
from flask import Flask, render_template, request, jsonify, json
import certifi
import time
from pymongo import MongoClient
app = Flask(__name__)

# mongoDB setting
import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

@app.route('/')
def home():
   return render_template('index.html')

# 구별 링크
@app.route('/detail')
def detail():
   dist = request.args.get('dist');
   return render_template('listpage.html', dist=dist)

@app.route('/detail/district', methods=["GET"])
def district() :
   searchDist = request.args.get("district")
   district_list = list(db.restaurants.find({'district':searchDist}, {'_id':False}).sort('starTotal', -1))
   result = [];
   for dining in district_list :
      item = {}
      item["restaurant_name"] = dining['name']
      item["restaurant_addr"] = dining['address']
      item["restaurant_kind"] = dining['kind']
      item["restaurant_district"] = dining['district']
      item["total_score"] = dining['starTotal']
      item["mango_score"] = dining['starMango']
      item["dining_score"] = dining['starDining']
      # print(db.imgs.find_one({"mangoID":dining['mangoID']}))
      item["restaurant_img"] = db.imgs.find_one({"mangoID":dining['mangoID']})['url']
      item["mangoId"] = dining['mangoID']   # 망고ID
      result.append(item)
   return jsonify({'result': result})

## 태성 code ##
@app.route('/detail/resDetail', methods=["GET"])
def detailPage():
    id = request.args.get('id')
    return render_template('review.html', id = id)

@app.route("/resDetail", methods=["GET"])
def res_Detail():
    resDetail = db.restaurants.find_one({'mangoID' : request.args.get('mangoId')},{'_id':False})
    imgList = list(db.imgs.find({'mangoID' : request.args.get('mangoId')},{'_id':False}))
    return jsonify({'resDetail' : resDetail, 'imgList' : imgList})

@app.route("/review", methods=["GET"])
def review_get():
    rows = list(db.reviews.find({}, {'_id': False}))
    bad = len(list(db.reviews.find({"score":"별로였어요"}, {'_id': False})))
    soso = len(list(db.reviews.find({"score":"괜찮았어요"}, {'_id': False})))
    good = len(list(db.reviews.find({"score":"맛있었어요"}, {'_id': False})))
    total = len(rows)

    return jsonify({'rows': rows,
                    'bad' : bad,
                    'soso' : soso,
                    'good' : good,
                    'total': total})

@app.route("/review", methods=["POST"])
def review_post():
    review_nickname_receive = request.form['review_nickname_give']
    review_comment_receive = request.form['review_comment_give']
    emotion_receive = request.form['emotion_give']

    now = time.localtime()
    detail_now = "%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    doc = {
        'nickname': review_nickname_receive,
        'comment' : review_comment_receive,
        'score' : emotion_receive,
        'time' : detail_now
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg': '댓글이 추가되었습니다!!'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=8000,debug=True)