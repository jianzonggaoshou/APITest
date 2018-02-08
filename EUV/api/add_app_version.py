# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""
增加app新的版本
"""

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://172.16.40.240:8080/sitopeuv/api/version/add.json"

data = {
    'version': '',
    'type': 1,
    'url': '',
    'flag': 0,
    'note': '版本说明'
}

response = session.post(url, data=data)

print(response.text)
