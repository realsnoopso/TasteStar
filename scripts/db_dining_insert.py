# db setting
from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tlsCAFile=certifi.where())
db = client.TasteStar

# scraping setting
import requests
from bs4 import BeautifulSoup

mangoName = list(db.restaurants.find({},{'_id':False}))
print(mangoName)
count = 0
for restaurantName in mangoName :
    count += 1
    diningName = restaurantName['name']
    diningAddress = restaurantName['address']
    diningMangoID = restaurantName['mangoID']
    db.restaurants.update_one({'mangoID': diningMangoID}, {'$set': {'starDining': 0}})
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.diningcode.com/list.php?query=' + diningName + '&rn=1',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    rows = soup.select('#div_list > li:nth-child(n+2)')

    for row in rows:
        name = row.select_one('a')
        if(name is None) :
            continue
        hrefLink = name['href']

        forHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        detailData = requests.get('https://www.diningcode.com' + hrefLink, headers=forHeader)
        detailDataPage = BeautifulSoup(detailData.text, 'html.parser')

        storeAddr = detailDataPage.select_one('#div_profile > div.s-list.basic-info > ul > li.locat').text
        if("서울특별시" in storeAddr) :
            storeAddr = storeAddr.replace("서울특별시", "서울시")
        elif ("서울" in storeAddr) :
            storeAddr = storeAddr.replace("서울", "서울시")
        if(diningAddress in storeAddr) :
            score = detailDataPage.select_one('#lbl_star_point > span.point')

            if(score is not None) :
                realScore = float(score.text.replace("점", ""))
                db.restaurants.update_one({'mangoID': diningMangoID}, {'$set': {'starDining': realScore}})
            break
    print(count)