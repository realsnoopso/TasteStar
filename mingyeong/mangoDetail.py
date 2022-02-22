import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 2. 망고플레이트 식당 상세 페이지 html 불러오기
sub = requests.get('https://www.mangoplate.com/restaurants/{}'.format('UifwVuxRDTSo'),headers=headers)
soup = BeautifulSoup(sub.text, 'html.parser')

# 이미지 가져오기
imgWrap = soup.select('body > main > article > aside.restaurant-photos > div')
for imgWrapList in imgWrap:
    target = imgWrapList.select('figure > img')

for url in target:
    final = url['src'].split(';*')[0]
    print(final)
