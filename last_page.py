import json

try:
    with open("data.json","r",encoding='utf-8') as f:
        json_object = json.load(f)
        next_page = json_object['page']
except:
    with open("data.json", 'w', encoding='utf-8') as f:
        next_page = 1