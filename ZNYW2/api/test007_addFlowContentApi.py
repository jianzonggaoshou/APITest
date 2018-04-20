# # coding=utf-8
# import requests
# from LoginPublic import LoginPublic
#
# """添加人员接口，给数据库添加人员，人员与角色挂钩"""
# # 使用requests中的Session方法获得session值
# session = requests.Session()
# LoginPublic.get_session(session)
#
# url = "http://www.sitop365.com/workflow/node/add"
#
# for i in range(0, 3):
#     # 数据
#     nodeNameList = ["确认", "审核", "验证"]
#     nodeNameValue = nodeNameList[i]
#     nodeDescriptionList = ["确认描述", "审核描述", "验证描述"]
#     nodeDescriptionValue = nodeDescriptionList[i]
#     userIdList = [[1353], [1355], [1353]]
# j
#     param = {"workflowId": 13,
#              "nodeName": nodeNameValue,
#              "nodeDescription": nodeDescriptionValue,
#              "userIdList": [1355],
#              "nodeParamList": [{"paramId": 56, "paramIsRequired": 0}, {"paramId": 57, "paramIsRequired": 0},
#                                {"paramId": 58, "paramIsRequired": 0}, {"paramId": 59, "paramIsRequired": 0},
#                                {"paramId": 59, "paramIsRequired": 0}, {"paramId": 60, "paramIsRequired": 0},
#                                {"paramId": 61, "paramIsRequired": 0}, {"paramId": 62, "paramIsRequired": 0},
#                                {"paramId": 63, "paramIsRequired": 0}, {"paramId": 64, "paramIsRequired": 0},
#                                {"paramId": 65, "paramIsRequired": 0}, {"paramId": 66, "paramIsRequired": 0},
#                                {"paramId": 67, "paramIsRequired": 0}, {"paramId": 66, "paramIsRequired": 0},
#                                {"paramId": 67, "paramIsRequired": 0}, {"paramId": 68, "paramIsRequired": 0},
#                                {"paramId": 69, "paramIsRequired": 0}, {"paramId": 70, "paramIsRequired": 0}]
#              }
#
#     # 传递的是json数据
#     headers = {"Content-Type": "application/json"}
#
#     response = session.post(url=url, data=str(param).encode('utf-8'), headers=headers)
#     print(response.text)
#     print(i)
