# coding=utf-8
import requests

from LoginPublic import LoginPublic

# 使用requests中的Session方法获得session值
session = requests.Session()
LoginPublic.get_session(session)

# api接口地址
url = "http://172.16.40.240:8080/sitopeuv/api/equipment/type/add.json"

datas = [
    {'equipmentTypeName': '设备类型1', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型2', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型3', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型4', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型5', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型6', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型7', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型8', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型9', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型10', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型11', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型12', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型13', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型14', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型15', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型16', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型17', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型18', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型19', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型20', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型21', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型22', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型23', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型24', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型25', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型26', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型27', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型28', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型29', 'equipmentTypeRemark': '测试分页'},
    {'equipmentTypeName': '设备类型30', 'equipmentTypeRemark': '测试分页'},
]

for data in datas:
    print data
    response = session.post(url=url, data=data)
    print(response.text)



