# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/emergency/add.json"

datas = [
    {'emergencyName': '紧急电话测试1', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试2', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试3', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试4', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试5', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试6', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试7', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试8', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试9', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试10', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试11', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试12', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试13', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试14', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试15', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试16', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试17', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试18', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试19', 'emergencyCall': '029-123456'},
    {'emergencyName': '紧急电话测试20', 'emergencyCall': '029-123456'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



