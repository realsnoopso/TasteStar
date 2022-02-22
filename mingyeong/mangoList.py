import requests
from bs4 import BeautifulSoup



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 1-1. 망고플레이트 지역별 식당 리스트 html 불러오기
guName = '중구'
main = requests.get('https://www.mangoplate.com/search/서울시%20{}'.format(guName),headers=headers)
soup1 = BeautifulSoup(main.text, 'html.parser')

# 1-2. 이름/음식 종류/별점/주소 정보 가져오기
list = soup1.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li')
for restaurant in list:
    name = restaurant.select_one('div > figure > figcaption > div > a > h2').text.split('(')[0].strip()
    kind = restaurant.select_one('div > figure > figcaption > div > p.etc > span').text
    starMango = restaurant.select_one('div > figure > figcaption > div > strong').text
    address = restaurant.select_one('div > figure > a > div > img')['alt'].split('- ')[1]
    mangoId = restaurant.select_one('div > figure > a')['href'].split('/')[2]
    print(name, kind, starMango, address, mangoId)


