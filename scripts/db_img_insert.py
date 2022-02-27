import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# db.imgs.delete_many({})   #img 테이블 삭제
# 식당 리스트 불러오기
restaurants = list(db.restaurants.find({},{'_id':False}))

for i in restaurants:
    id = i['mangoID']

# 1. 망고플레이트 식당 상세 정보 html 불러오기
    gu = requests.get('https://www.mangoplate.com/restaurants/{}'.format(id),headers=headers)
    soup = BeautifulSoup(gu.text, 'html.parser')
    list = soup.select('body > main > article > aside.restaurant-photos > div')

    for li in list:
        img = li.select('figure.list-photo')
        cnt = 0

        for i in img:

            im = i.select_one('figure > img')['src'].split(';')
            print(im[0])
            cnt = cnt + 1

            imgJson = {
                   'mangoID': id,
                   'sequence': cnt,
                   'url': im[0],
            }
            db.imgs.insert_one(imgJson)

            if cnt == 4:
                break
