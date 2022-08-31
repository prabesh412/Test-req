import requests
import json


url = "https://bg.annapurnapost.com/api/search?page=1&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"
payload = {}
headers = {}
response = requests.request("GET", url,timeout=10, headers=headers, data=payload)
data = response.json()
last = data['data']['totalPage']
with open("data.json","r",encoding='utf-8') as f:
    try:
        json_object = json.load(f)
        for i in json_object:
            next_page = i['page']
    except:
        next_page = 1

def request(page, last_page):
    dictobj=[]
    for r in range(page, last_page):
        url = f"https://bg.annapurnapost.com/api/search?page={page}&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"

        payload={}
        headers = {}
        res = []
        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()

        for i in data['data']['items']:

            res.append(i["title"])

        page += 1

        dictobj.append({"page": page - 1,
                        "title": res})
        with open('data.json', 'r+', encoding='utf-8') as json_file:
            try:
                listobj = json.load(json_file)
                listobj.append({"page": page - 1,"title": res})

                with open('data.json', 'w', encoding='utf-8') as json_file:
                    json.dump(listobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))
            except:
                with open('data.json', 'w', encoding='utf-8') as json_file:
                    json.dump(dictobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))
request(next_page,last)