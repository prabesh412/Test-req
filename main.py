import requests
import json

def request(page, last):
    res = []
    dictobj = {}
    result = []
    for r in range(page, last+1):
        url = f"https://bg.annapurnapost.com/api/search?page={page}&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        for i in data['data']['items']:
            res.append(i["title"])
        for j in res:
            result.append(j)
        page += 1

    dictobj["title"] =res

    try:
        with open('data.json', 'r+', encoding='utf-8') as json_file:
            listobj = json.load(json_file)
            listobj["title"] += res
            dictobj["title"] = listobj["title"]
    except:
        print("error")
        
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(dictobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))

request(4,10)