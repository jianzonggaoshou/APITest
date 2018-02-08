# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/role/add.json"

datas = [
    {'roleName': '角色测试1', 'roleRemark': '测试分页'},
    {'roleName': '角色测试2', 'roleRemark': '测试分页'},
    {'roleName': '角色测试3', 'roleRemark': '测试分页'},
    {'roleName': '角色测试4', 'roleRemark': '测试分页'},
    {'roleName': '角色测试5', 'roleRemark': '测试分页'},
    {'roleName': '角色测试6', 'roleRemark': '测试分页'},
    {'roleName': '角色测试7', 'roleRemark': '测试分页'},
    {'roleName': '角色测试8', 'roleRemark': '测试分页'},
    {'roleName': '角色测试9', 'roleRemark': '测试分页'},
    {'roleName': '角色测试10', 'roleRemark': '测试分页'},
    {'roleName': '角色测试11', 'roleRemark': '测试分页'},
    {'roleName': '角色测试12', 'roleRemark': '测试分页'},
    {'roleName': '角色测试13', 'roleRemark': '测试分页'},
    {'roleName': '角色测试14', 'roleRemark': '测试分页'},
    {'roleName': '角色测试15', 'roleRemark': '测试分页'},
    {'roleName': '角色测试16', 'roleRemark': '测试分页'},
    {'roleName': '角色测试17', 'roleRemark': '测试分页'},
    {'roleName': '角色测试18', 'roleRemark': '测试分页'},
    {'roleName': '角色测试19', 'roleRemark': '测试分页'},
    {'roleName': '角色测试20', 'roleRemark': '测试分页'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



