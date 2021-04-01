#-*- coding: utf-8 -*-
import requests
import json
import os

file1 = open("test.txt",'r')

while True:
    lines = file1.readline()
    url = lines
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
    if not lines:
        break
file1.close()   