import requests
import json

url = "https://bg.annapurnapost.com/api/search?page=1&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"
payload = {}
headers = {}
response = requests.request("GET", url,timeout=10, headers=headers, data=payload)
data = response.json()
last = data['data']['totalPage']
try:
    with open("data.json","r",encoding='utf-8') as f:
        json_object = json.load(f)
        for i in json_object:
            next_page = i['page'] + 1
except:
    with open("data.json", 'w', encoding='utf-8') as f:
        next_page = 1