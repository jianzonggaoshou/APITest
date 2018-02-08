# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://172.16.40.240:8080/sitopeuv/api/equipment/type/page/list.json"

response = session.get(url)

print(response.text)

