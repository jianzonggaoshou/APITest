# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/room/add.json"

datas = [
    {'roomName': '电机配电室03', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室04', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室05', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室06', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室07', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室08', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室09', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室10', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室11', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室12', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室13', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室14', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室15', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室16', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室17', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室18', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室19', 'roomType': '1', 'roomRemark': '测试分页'},
    {'roomName': '电机配电室20', 'roomType': '1', 'roomRemark': '测试分页'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



