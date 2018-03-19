# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""添加配电室接口"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/substation/add"

for i in range(1, 101):
    # 数据
    substationNameValue = str(i) + '@测试配电室'

    param = {"substationName": substationNameValue,
             "voltageLevelCode": "220V",
             "substationId": "",
             "customerId": 1253}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
