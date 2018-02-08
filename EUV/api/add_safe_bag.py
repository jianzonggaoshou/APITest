# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/bag/security/add.json"

datas = [
    {'securityName': '安全包测试1', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试2', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试3', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试4', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试5', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试6', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试7', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试8', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试9', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试10', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试11', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试12', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试13', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试14', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试15', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试16', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试17', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试18', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试19', 'securityRemark': '测试分页'},
    {'securityName': '安全包测试20', 'securityRemark': '测试分页'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



