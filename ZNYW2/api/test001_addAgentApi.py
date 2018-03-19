# coding=utf-8
import requests
from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/agent/add"

for i in range(1, 11):
    # 数据
    agentNameValue = "test服务商" + str(i)
    agentLinkmanValue = "许臻" + str(i)
    agentShortNamePinyinValue = "TEST" + str(i)
    userNameValue = "agentUser" + str(i)
    realNameValue = "许臻" + str(i)

    param = {
             "agentId": "",
             "agentName": agentNameValue,
             "agentShortNamePinyin": agentShortNamePinyinValue,
             "agentLinkman": agentLinkmanValue,
             "agentLinkPhone": "15609100803",
             "regionId": 2,
             "agentState": 0,
             "agentRegisterTime": 1521388800000,
             "agentExpiryTime": 1525276800000,
             "agentAddress": "软件新城二期",
             "agentPic": "",
             "username": userNameValue,
             "password": "123456",
             "passwordAgain": True,
             "realName": realNameValue,
             "mobile": "15609100803",
             "permissionIds": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28"}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
