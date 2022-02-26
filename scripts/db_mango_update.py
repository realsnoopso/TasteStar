# mongoDB setting
import certifi
import pymongo

# 스케줄 모듈
import schedule
import time

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    tlsCAFile=ca)
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

districts = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구',
             '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']


def insert_db(districts, headers):
    output_list = []

    for district in districts:
        data = requests.get('https://www.mangoplate.com/search/서울시%20{}'.format(district), headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        restaurants = soup.select(
            'body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li > div.list-restaurant-item')
        for restaurant in restaurants:
            name = restaurant.select_one('figure > figcaption > div > a > h2').text.split('(')[0].strip()
            kind = restaurant.select_one('figure > figcaption > div > p.etc > span').text
            address = restaurant.select_one('figure > a > div > img')['alt'].split('- ')[1]
            mangoID = restaurant.select_one('figure > a')['href'].split('/')[2]
            district = address.split(' ')[1]
            starMango = restaurant.select_one('figure > figcaption > div > strong').text

            if starMango == '':
                starMango = 0
            else:
                starMango = float(starMango)

            output = {
                'address': address,
                'kind': kind,
                'name': name,
                'starMango': starMango,
                'mangoID': mangoID,
                'district': district
            }

            output_list.append(output)


    return output_list


def job():
    for element in insert_db(districts, headers):
        db.test3.update_one({}, {'$set': element})

schedule.every().monday.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)