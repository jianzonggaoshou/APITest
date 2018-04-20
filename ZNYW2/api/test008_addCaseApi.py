# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""代理商增加接口，给数据库添加代理商及代理商管理员"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# url = "http://www.sitop365.com/agent/add"
url = "http://172.16.40.240:7777/case/add"

for i in range(1, 101):
    # 数据
    caseTitle = "test案例名称" + str(i)

    param = {
        "caseContent": "<p>案例名称</p>",
        "caseTitle": caseTitle

    }

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
