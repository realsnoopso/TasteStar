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

# 구 리스트 불러오기
guNames = list(db.districts.find({},{'_id':False}))




# 2. 이름/음식 종류/별점/주소 정보 DB에 저장하기

for i in guNames:
    guName = i['name']
    print(guName)

# 1. 망고플레이트 지역별 식당 리스트 html 불러오기
gu = requests.get('https://www.mangoplate.com/search/서울시%20{}'.format(guName[0]),headers=headers)
soup1 = BeautifulSoup(main.text, 'html.parser')

list = soup1.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')
for restaurant in list:
    name = restaurant.select_one('div > figure > figcaption > div > a > h2').text.split('(')[0].strip()
    kind = restaurant.select_one('div > figure > figcaption > div > p.etc > span').text
    starMango = restaurant.select_one('div > figure > figcaption > div > strong').text
    address = restaurant.select_one('div > figure > a > div > img')['alt'].split('- ')[1]
    mangoID = restaurant.select_one('div > figure > a')['href'].split('/')[2]
    restaurant = {
        'address': address,
        'kind': kind,
        'name': name,
        'starMango': starMango,
        'mangoID': mangoID
    }
    db.restaurants.insert_one(restaurant)

# 00:00에 DB 업데이트하기