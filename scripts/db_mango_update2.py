import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 식당 불러오기
restaurants = list(db.restaurants.find({},{'_id':False}))

for i in restaurants:
    id = i['mangoID']

# 1. 망고플레이트 식당 상세 정보 html 불러오기
    gu = requests.get('https://www.mangoplate.com/restaurants/{}'.format(id),headers=headers)
    soup = BeautifulSoup(gu.text, 'html.parser')

    list = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr')

    td1 = ""
    td2 = ""
    for li in list:

        th1 = li.select_one('tr > th').text

        if th1 == '영업시간':
            td1 = li.select_one('tr > td').text
        if th1 == '전화번호':
            td2 = li.select_one('tr > td').text

    print('영업시간 : ' + td1, '전화번호 : ' + td2)
# 2. db 업데이트
    db.restaurants.update_one({'mangoID': id}, {'$set': {'businesshours': td1}})
    db.restaurants.update_one({'mangoID': id}, {'$set': {'tel': td2}})

