#-*- coding: utf-8 -*-
import requests
import json

url = 'http://api.k780.com:88/?app=phone.get&phone=13093452121&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json'
parms={}
r = requests.get(url)
assert r.status_code == 200,"连接出错"
d = json.loads(r.text)
if d['success'] == "1":
    print("检查通过")
    with open("test1.json", 'w', encoding='utf-8')as f:
        json.dump(json.loads(r.text), f,ensure_ascii=False)
        f.close()
else:
    print("检查不通过")