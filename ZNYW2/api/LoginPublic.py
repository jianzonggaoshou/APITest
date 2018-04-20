# coding=utf-8
class LoginPublic:
    def __init__(self):
        pass

    @staticmethod
    def get_session(session):
        # url = "http://www.sitop365.com/login"
        url = "http://172.16.40.240:7777/login"

        # params = {"username": "agentUser1", "password": "123456"}
        params = {"username": "test", "password": "123456"}

        headers = {}
        # 请求登录服务器获取session值
        session.post(url, data=params, headers=headers)
