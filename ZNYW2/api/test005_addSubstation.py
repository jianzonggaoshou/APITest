# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""添加配电室接口"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/user/add"

for i in range(0, 3):
    # 数据
    roleIdList = [1173, 1174, 1175]
    roleIdValue = roleIdList[i]
    userNameList = ['Diaodu101', 'Jiankong101', 'Xianxia101']
    userNameValue = userNameList[i]
    realNameList = ['调度人员', '监控人员', '线下人员']
    realNameValue = realNameList[i]

    param = {"agentId": 22,
             "customerId": "",
             "roleId": roleIdValue,
             "username": userNameValue,
             "password": "123456",
             "realName": realNameValue,
             "mobile": "15609100803"}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
