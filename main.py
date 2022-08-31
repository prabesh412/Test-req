import requests
import pandas as pd
from pandas import *
import json

url = "https://bg.annapurnapost.com/api/tags/news?page=1&per_page=40&tag=corona-virus"

payload={}
headers = {}
res = []
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
for i in data['data']:
    res.append(i)

df = pd.json_normalize(res)
df.to_csv('result.csv')

data = read_csv("result.csv")
slug = data['title'].tolist()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({"titles":slug}, f, ensure_ascii=False, indent=4)