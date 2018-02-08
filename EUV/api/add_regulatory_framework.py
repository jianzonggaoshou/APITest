# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/regulation/add.json"

datas = [
    {'regulationName': '规章制度测试1', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试2', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试3', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试4', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试5', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试6', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试7', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试8', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试9', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试10', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试11', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试12', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试13', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试14', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试15', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试16', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试17', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试18', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试19', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},
    {'regulationName': '规章制度测试20', 'createPersonName': '许臻', 'createDeptName': '研发部', 'implStartTime': '2018-01-31', 'regulationContent': '规章制度测试'},

]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



