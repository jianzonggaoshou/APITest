# coding=utf-8
import requests
from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/role/add"

for i in range(0, 3):
    # 数据
    roleNameList = ['调度人员', '监控人员', '线下人员']
    roleNameValue = roleNameList[i]

    param = {"agentId": 22,
             "customerId": "",
             "roleId": "",
             "selOn": True,
             "roleName": roleNameValue,
             "permissionIds": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28"}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
