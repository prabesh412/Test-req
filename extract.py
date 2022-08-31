import json

with open('data.json', 'r', encoding='utf-8') as json_file:
    titles = json.load(json_file)
    for i in titles["title"]:
        print(i)
