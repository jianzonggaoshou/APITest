# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/bag/job/add.json"

datas = [
    {'jobName': '作业包测试1', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试2', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试3', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试4', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试5', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试6', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试7', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试8', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试9', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试10', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试11', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试12', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试13', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试14', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试15', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试16', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试17', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试18', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试19', 'jobRemark': '测试分页'},
    {'jobName': '作业包测试20', 'jobRemark': '测试分页'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



