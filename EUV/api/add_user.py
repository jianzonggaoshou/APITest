# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://172.16.40.240:8080/sitopeuv/user/add.json"

data = {
    'userName': 'xjzyA01',
    'userPwd': '123456',
    'realName': '巡检组员A01',
    'userPhone': '15609100010',
    'userTelephone': '029-123456',
    'roleIds': '33',
    'deptIds': '224',
    'userType': '2'
}

response = session.post(url, data=data)

print(response.text)