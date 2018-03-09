# coding=utf-8
import requests
from LoginPublic import LoginPublic
import csv

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://39.107.121.205:8080/equipment/add"

with open('equipmentList.csv', 'r') as csvFile:
    text = csv.reader(csvFile)
    print(text)
    for data in text:
        print(data)
        data = ''.join(data)
        print(data)

        param = {"substationId": 4,
                 "equipmentId": "",
                 "equipmentName": data,
                 "serialNumber": "",
                 "voltageLevelCode": "10kV",
                 "equipmentTypeId": 1,
                 "startUseTime": 1514217600000}

        print(param)

        headers = {}

        response = session.post(url=url, data=param, headers=headers)
        print(response.text)


