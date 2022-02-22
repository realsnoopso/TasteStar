# mongoDB setting
import certifi
import pymongo
import time
import schedule

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 1. mongoDB에서 저장된 구 리스트 불러오기
guName = list(db.districts.find({},{'_id':False}))

# 2. html 긁어오는 것을 반복하기
for i in guName:
    district = i['name']
    # print (district)
    for ii in district:
        list = BeautifulSoup(requests.get('https://www.mangoplate.com/search/서울시%20{}'.format(ii), headers = headers).text, 'html.parser').select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')

# 3. 구별 식당 정보 가져오기
        for restaurant in list:
            name = restaurant.select_one('div > figure > figcaption > div > a > h2').text.split('(')[0].strip()
            kind = restaurant.select_one('div > figure > figcaption > div > p.etc > span').text
            starMango = restaurant.select_one('div > figure > figcaption > div > strong').text
            address = restaurant.select_one('div > figure > a > div > img')['alt'].split('- ')[1]
            mangoID = restaurant.select_one('div > figure > a')['href'].split('/')[2]
            output = {
                'address': address,
                'kind': kind,
                'name': name,
                'starMango': starMango,
                'mangoID': mangoID,
                'district': district
            }

            db.restaurants.insert_one(output)