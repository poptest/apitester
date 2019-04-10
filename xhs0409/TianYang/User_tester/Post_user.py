import unittest
import requests
from config import HOST


class Postuser(unittest.TestCase):

    def test_case01(self):
    #一切参数正常输入
        user_url= HOST + "user"

        user_data = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }

        resp = requests.post(user_url, data=user_data)

        Expected = 200

        Actual = resp.status_code

        # resp = requests.post(user_url, data=user_data)
        # print(resp.status_code)
        # print(resp.content)
        self.assertEqual(Expected,Actual,msg='注册成功')

        print(resp.content)


    #username中含有特殊字符
    def test_case02(self):
        user_url = HOST + "user"

        user_data = {
            "username": "p@op4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }

        resp= requests.post(user_url, data=user_data)

        #期望值
        exc=400

        #实际值
        act = resp.status_code

        resp = requests.post(user_url, data=user_data)

        self.assertDictEqual(exc,act,msg='注册失败')

        # print(resp.status_code)
        print(resp.content)

    #email中无@字符
    def test_case03(self):
        user_url = HOST + "user"

        user_data = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwertqq.com",
            "password": "123456"
        }

        resp = requests.post(user_url, data=user_data)

        Expected = 400

        Actual = resp.status_code
        self.assertDictEqual(Expected,Actual, msg='注册失败')

        # print(resp.status_code)
        print(resp.content)


    #tel字符长度为七位
    def test_004(self):

        user_url = HOST + "user"
        # print(user_url)

        user_data = {
            "username": "pop4",
            "tel": "1573846",
            "email": "qwert@qq.com",
            "password": "123456"
        }

        resp = requests.post(user_url, data=user_data)

        Expected = 400

        Actual = resp.status_code
        self.assertDictEqual(Expected, Actual,msg='注册失败')

        # print(resp.status_code)
        print(resp.content)
    #passw含有特殊字符
    def test_005(self):
        user_url = HOST + "user"



        user_data = {
            "username": "pop6",
            "tel": "15738460225",
            "email": "157@qq.com",
            "password": "1521@234"
        }
        resp = requests.post(user_url, data=user_data)

        Expected = 400

        Actual = resp.status_code
        self.assertDictEqual(Expected,Actual,msg='注册失败')

        # print(resp.status_code)
        print(resp.content)


    #tel长度为12位
    def test_case006(self):
        user_url = HOST + "user"

        user_data = {
            "username": "pop6",
            "tel": "157384602251",
            "email": "157@qq.com",
            "password": "1521@234"
        }
        resp = requests.post(user_url, data=user_data)

        Expected = 400

        Actual = resp.status_code
        self.assertDictEqual(Expected, Actual, msg='注册失败')

        # print(resp.status_code)
        print(resp.content)
if __name__ == '__main__':
    unittest.main()