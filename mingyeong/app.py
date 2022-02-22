import certifi
import pymongo
import mangoList
import mangoDetail


ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://sparta19:toyproject@cluster0.rrg9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.dbsparta

print(mangoList.name, mangoList.kind, mangoList.starMango, mangoList.address)

print(mangoDetail.url['src'])