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


data = requests.get('https://www.mangoplate.com/search/서울시%20{}'.format('강남구'),headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
restaurants = soup.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li > div.list-restaurant-item')

for restaurant in restaurants:
    name = restaurant.select_one('figure > figcaption > div > a > h2').text.split('(')[0].strip()
    kind = restaurant.select_one('figure > figcaption > div > p.etc > span').text
    starMango = restaurant.select_one('figure > figcaption > div > strong').text
    address = restaurant.select_one('figure > a > div > img')['alt'].split('- ')[1]
    mangoID = restaurant.select_one('figure > a')['href'].split('/')[2]
    district = address.split(' ')[1]
    output = {
        'address': address,
        'kind': kind,
        'name': name,
        'starMango': starMango,
        'mangoID': mangoID,
        'district': district
    }

    print(district, '-', name, kind, starMango, address, mangoID)
    db.restaurants.insert_one(output)