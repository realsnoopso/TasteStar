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

# 1. mongoDB에서 저장된 구 리스트 불러오기


# star = db.restaurants.find({'name':''})
# print(star)
            # for ii in output:
            #     db.restaurants.update_one({}, {'$set': {'starMango': starMango}})
            # schedule.every().monday.at("00:00").do(printhello)

for i in guName:
    district = i['name']
    for ii in district:
        list = BeautifulSoup(requests.get('https://www.mangoplate.com/search/서울시%20{}'.format(ii), headers=headers).text,'html.parser').select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')
        guName = list(db.districts.find({}, {'_id': False}))


