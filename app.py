# flask setting
from flask import Flask, render_template
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

@app.route('/jongno')
def jongno():
   return render_template('district/jongno.html')

@app.route('/jung')
def jung():
   return render_template('district/jung.html')

@app.route('/yongsan')
def yongsan():
   return render_template('district/yongsan.html')

@app.route('/seongdong')
def seongdong():
   return render_template('district/seongdong.html')

@app.route('/gwangjin')
def gwangjin():
   return render_template('district/gwangjin.html')

@app.route('/dongdaemun')
def dongdaemun():
   return render_template('district/dongdaemun.html')

@app.route('/jungnang')
def jungnang():
   return render_template('district/jungnang.html')

@app.route('/seongbuk')
def seongbuk():
   return render_template('district/seongbuk.html')

@app.route('/gangbuk')
def gangbuk():
   return render_template('district/gangbuk.html')

@app.route('/dobong')
def dobong():
   return render_template('district/dobong.html')

@app.route('/nowon')
def nowon():
   return render_template('district/nowon.html')

@app.route('/eunpyeong')
def eunpyeong():
   return render_template('district/eunpyeong.html')

@app.route('/seodaemun')
def seodaemun():
   return render_template('district/seodaemun.html')

@app.route('/mapo')
def mapo():
   return render_template('district/mapo.html')

@app.route('/yangcheon')
def yangcheon():
   return render_template('district/yangcheon.html')

@app.route('/gangseo')
def gangseo():
   return render_template('district/gangseo.html')

@app.route('/guro')
def guro():
   return render_template('district/guro.html')

@app.route('/geumcheon')
def geumcheon():
   return render_template('district/geumcheon.html')

@app.route('/yeongdeungpo')
def yeongdeungpo():
   return render_template('district/yeongdeungpo.html')

@app.route('/dongjak')
def dongjak():
   return render_template('district/dongjak.html')

@app.route('/gwanak')
def gwanak():
   return render_template('district/gwanak.html')

@app.route('/seocho')
def seocho():
   return render_template('district/seocho.html')

@app.route('/gangnam')
def gangnam():
   return render_template('district/gangnam.html')

@app.route('/songpa')
def songpa():
   return render_template('district/songpa.html')

@app.route('/gangdong')
def gangdong():
   return render_template('district/gangdong.html')



if __name__ == '__main__':
   app.run('0.0.0.0',port=8000,debug=True)