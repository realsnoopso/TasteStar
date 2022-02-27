from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tlsCAFile=certifi.where())
db = client.TasteStar

# starList =  db.restaurants.find_one({'name':'FOURB'})
# print(starList)

starList =  list(db.restaurants.find({},{'_id':False}))
count = 1
for score in starList :
    starM = score['starMango']
    starD = score['starDining']
    print(count, score['name'])
    count += 1
    print(count)
    if (starD == 0) :
        db.restaurants.update_one({'mangoID': score['mangoID']}, {'$set': {'starTotal': starM}})
    else:
        db.restaurants.update_one({'mangoID': score['mangoID']}, {'$set': {'starTotal': round((starM + starD)/2,1)}})