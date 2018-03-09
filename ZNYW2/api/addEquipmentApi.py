# coding=utf-8
import requests
from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

url = "http://39.107.121.205:8080/equipment/add"

params = [
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室3@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室4@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室5@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室6@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室7@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室8@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室9@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室10@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室11@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室12@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室13@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室14@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室15@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室16@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室17@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室18@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室19@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    # {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室20@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室21@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室22@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室23@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室24@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室25@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室26@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室27@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室28@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室29@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室30@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室31@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室32@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室33@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室34@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室35@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室36@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室37@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室38@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室39@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室40@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室41@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室42@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室43@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室44@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室45@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室46@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室47@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室48@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室49@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},
    {"substationId": 4, "equipmentId": "", "equipmentName": "高压配电室50@变压器", "serialNumber": "", "voltageLevelCode": "10kV", "equipmentTypeId": 1, "startUseTime": 1514217600000},




]

headers = {}

for param in params:
    print param
    response = session.post(url=url, data=param, headers=headers)
    print(response.text)


