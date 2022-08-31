import requests
import json
from object import last, next_page

def request(page, last_page):
    dictobj=[]
    for r in range(page, last_page+1):
        url = f"https://bg.annapurnapost.com/api/search?page={page}&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"

        payload={}
        headers = {}
        res = []
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        for i in data['data']['items']:
            res.append(i["title"])

        dictobj.append({"page": page,"title": res})
        page += 1
        try:
            with open('data.json', 'r+', encoding='utf-8') as json_file:
                listobj = json.load(json_file)
                listobj.append({"page": page - 1,"title": res})

                with open('data.json', 'w', encoding='utf-8') as json_file:
                    json.dump(listobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))
        except:
            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(dictobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))

request(next_page,last)