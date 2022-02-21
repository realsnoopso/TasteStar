import requests
import json
url = "https://data.mongodb-api.com/app/data-dciya/endpoint/data/beta/action/findOne"
payload = json.dumps({
    "collection": "users",
    "database": "dbsparta",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '62138400fd368f8772ccb4e6'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)