# mongoDB setting
import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 구 이름 붙여넣기
districts = [
    {'name': '강남구'},
    {'name': '강동구'},
    {'name': '강북구'},
    {'name': '강서구'},
    {'name': '관악구'},
    {'name': '광진구'},
    {'name': '구로구'},
    {'name': '금천구'},
    {'name': '노원구'},
    {'name': '도봉구'},
    {'name': '동대문구'},
    {'name': '동작구'},
    {'name': '마포구'},
    {'name': '서대문구'},
    {'name': '서초구'},
    {'name': '성동구'},
    {'name': '성북구'},
    {'name': '송파구'},
    {'name': '양천구'},
    {'name': '영등포구'},
    {'name': '용산구'},
    {'name': '은평구'},
    {'name': '종로구'},
    {'name': '중구'},
    {'name': '중랑구'}
]

for district in districts:
    db.districts.insert_one(district)



