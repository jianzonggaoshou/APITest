# coding=utf-8
class LoginPublic:
    def __init__(self):
        pass

    @staticmethod
    def get_session(session):
        url = "http://39.107.121.205:8080/login"

        params = {"username": "agentxuzhen", "password": "123456"}

        headers = {}
        # 请求登录服务器获取session值
        session.post(url, data=params, headers=headers)
