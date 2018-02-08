# coding:utf-8
class LoginPublic:
    def __init__(self):
        pass

    @staticmethod
    def get_session(session):
        url = "http://172.16.40.240:8080/sitopeuv/api/user/login.json"

        params = {"userName": "15609100803", "userPwd": "123456"}

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        # 请求登录服务器获取session值
        response = session.post(url, data=params, headers=headers)
        print response
        print str(params) + '登录成功'


