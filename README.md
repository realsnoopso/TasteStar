### Description

* 지역별 맛집의 서비스별 별점을 한 눈에 볼 수 있는 서비스입니다.

### Environment
* python 3.8


### Prerequisite
* certifi
* pymongo
* requests
* BeautifulSoup

### Files
* mingyeong
  * app.py: 크롤링 정보를 DB에 업데이트
  * mangoDetail: 망고플레이스 식당 상세 페이지 크롤링
  * mangoList: 망고플레이스 지역별 식당 TOP 10 리스트 크롤링
