# coding=utf-8
import requests
from LoginPublic import LoginPublic
import random

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/customer/add"

for i in range(11, 31):
    # 数据
    customerNameValue = "test测试客户" + str(i)
    longitudeValue = random.randint(100, 200)
    latitudeValue = random.randint(10, 100)
    userNameValue = "customerUserD" + str(i)

    param = {
             "customerId": "",
             "customerName": customerNameValue,
             "customerLinkman": "许臻",
             "customerPhone": "15609100803",
             "agentId": 22,
             "regionId": 2,
             "customerState": 0,
             "customerType": 1,
             "customerRegisterTime": 1521388800000,
             "customerExpiryTime": 1528387200000,
             "longitude": longitudeValue,
             "latitude": latitudeValue,
             "customerAddress": "软件新城二期",
             "customerIntroduction": "客户介绍",
             "customerPic": "",
             "username": userNameValue,
             "password": "123456",
             "passwordAgain": True,
             "realName": "许臻",
             "mobile": "15609100803",
             "permissionIds": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28"}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
