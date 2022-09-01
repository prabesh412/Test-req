import requests
import json
from last_page import next_page

def request(page, last):
    if page == 1:
        json_template = {
        "title": [],
        "page": 1}
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_template, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))

    with open('data.json', 'r+', encoding='utf-8') as json_file:
        listobj = json.load(json_file)

    for r in range(page, last+1):
        res = []
        url = f"https://bg.annapurnapost.com/api/search?page={page}&title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        for i in data['data']['items']:
            res.append(i["title"])
        page += 1
        listobj["title"] += res
        listobj["page"] = page - 1
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(listobj, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))

request(next_page,10)