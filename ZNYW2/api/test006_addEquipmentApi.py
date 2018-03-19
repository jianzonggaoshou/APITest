# coding=utf-8
import requests
from LoginPublic import LoginPublic

"""添加设备接口"""
# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://www.sitop365.com/equipment/add"

for i in range(1, 101):
    # 数据
    equipmentNameValue = '2@测试配电室' + str(i) + '#测试设备'
    serialNumberValue = 'SITO' + str(i)

    param = {"equipmentName": equipmentNameValue,
             "equipmentTypeId": 1,
             "voltageLevelCode": "220V",
             "serialNumber": serialNumberValue,
             "startUseTime": 1521388800000,
             "substationId": 156,
             "equipmentId": ""}

    headers = {}

    response = session.post(url=url, data=param, headers=headers)
    print(response.text)
    print(i)
