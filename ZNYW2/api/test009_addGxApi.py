# coding=utf-8
import requests
from LoginPublic import LoginPublic
import random

"""代理商增加接口，给数据库添加代理商及代理商管理员"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# url = "http://www.sitop365.com/agent/add"
url = "http://172.16.40.240:7777/user/add"

for i in range(12, 31):
    # 数据
    username = "gx" + str(i)
    realname = "test共享电工" + str(i)
    mobile = random.randint(15609100001, 15609109999)

    param = {
        "agentId": 17,
        "customerId": "",
        "roleId": 165,
        "username": username,
        "password": "123456",
        "realName": realname,
        "mobile": mobile,
    }

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
