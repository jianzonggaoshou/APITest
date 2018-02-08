# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""
获得最新客户版app版本
"""

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://172.16.40.240:8080/sitopeuv/api/version/latestCustomerApp.json"

data = {}

response = session.post(url, data=data)

print(response.text)
