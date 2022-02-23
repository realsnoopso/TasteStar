import certifi
import pymongo
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.TasteStar

img = {
    'sequence': 'test',
    'url': 'test'
}

restaurant = {'address':'test',
       'businesshours': 'test',
       'guName': 'test',
       'kind': 'test',
       'name': 'test',
       'starDining': 'test',
       'starMango': 'test',
       'starTotal': 'test',
       'tel': 'test'}

review = {
    'comment': 'test',
    'nickname': 'test',
    'score': 'test',
    'time': 'test',
}

db.imgs.insert_one(img)
db.restaurants.insert_one(restaurant)
db.reviews.insert_one(review)