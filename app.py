from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient
import time

ca = certifi.where()
client = MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar
app = Flask(__name__)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail/detailreview')
def detailreview():
    return render_template('review.html', id=request.args.get('id'))

@app.route("/resDetail", methods=["GET"])
def res_Detail():
    resDetail = db.restaurants.find_one({'mangoID' : request.args.get('mangoId')},{'_id':False})
    imgList = list(db.imgs.find({'mangoID' : request.args.get('mangoId')},{'_id':False}))
    return jsonify({'resDetail' : resDetail, 'imgList' : imgList})

@app.route("/detail/resDetail", methods=["GET"])
def review_get():
    rows = list(db.reviews.find({"pageID":request.args.get('mangoId')}, {'_id': False}))
    bad = len(list(db.reviews.find({"score":"별로였어요","pageID":request.args.get('mangoId')}, {'_id': False})))
    soso = len(list(db.reviews.find({"score":"괜찮았어요","pageID":request.args.get('mangoId')}, {'_id': False})))
    good = len(list(db.reviews.find({"score":"맛있었어요","pageID":request.args.get('mangoId')}, {'_id': False})))
    total = len(rows)

    pageid = db.reviews.find({"pageID": request.args.get('mangoId')}, {'_id': False})

    return jsonify({'rows': rows,
                    'bad' : bad,
                    'soso' : soso,
                    'good' : good,
                    'total': total,
                    'pageid': pageid
                    })

@app.route("/detail/resDetail", methods=["POST"])
def review_post():
    review_nickname_receive = request.form['review_nickname_give']
    review_comment_receive = request.form['review_comment_give']
    emotion_receive = request.form['emotion_give']
    pageid = request.form['pageid']

    now = time.localtime()
    detail_now = "%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    doc = {
        'nickname': review_nickname_receive,
        'comment' : review_comment_receive,
        'score' : emotion_receive,
        'time' : detail_now,
        'pageid': pageid
    }
    db.reviews.insert_one(doc)
    return jsonify({'msg': '댓글이 추가되었습니다!!'})

# 구별 링크
@app.route('/detail')
def detail():
   dist = request.args.get('dist');
   return render_template('listpage.html', dist=dist)

@app.route('/detail/district', methods=["GET"])
def district() :
   searchDist = request.args.get("district")
   district_list = list(db.restaurants.find({'district':searchDist}, {'_id':False}).sort('starTotal', -1))
   result = []
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

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)