# coding=utf-8
import requests
from LoginPublic import LoginPublic
import random

"""客户增加接口，给数据库添加客户及客户管理员"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# url = "http://www.sitop365.com/customer/add"
url = "http://172.16.40.240:7777/customer/add"

for i in range(3, 21):
    # 数据
    customerNameValue = "test测试客户" + str(i)
    customerLinkman = "许臻" + str(i)
    customerPhone = random.randint(15609100001, 15609109999)
    longitudeValue = random.randint(100, 200)
    latitudeValue = random.randint(10, 100)
    userNameValue = "customerTest" + str(i)

    param = {
             "tit": "新增客户",
         "type": 1,
         "customerId": "",
         "customerName": customerNameValue,
         "customerLinkman": customerLinkman,
         "customerPhone": customerPhone,
         "agentId": 1,
         "regionId": "",
         "customerState": 0,
         "customerType": 1,
         "customerRegisterTime": 1523808000000,
         "customerRegisterTimeElse": "2018-04-15T16:00:00.000Z",
         "customerExpiryTime": 1523808000000,
         "customerExpiryTimeElse": "2018-04-15T16:00:00.000Z",
         "longitude": longitudeValue,
         "latitude": latitudeValue,
         "customerAddress": "",
         "customerIntroduction": "",
         "customerPic": "",
         "username": userNameValue,
         "password": "123456",
         "passwordAgain": True,
         "realName": "123213",
         "mobile": customerPhone,
         "permissionIds": "1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18",
    }

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
