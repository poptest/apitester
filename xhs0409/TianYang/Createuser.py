import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):

    def test_case01(self):
        # 改变password字符长度
        user_url = HOST + "/user"
        # 期望值
        exp_value = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        # 实际值
        user_data = {
            "username": "pop4",
            "tel": "1573846",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        # resp = requests.post(user_url, data=user_data)
        # print(resp.status_code)
        # print(resp.content)
        self.assertDictEqual(user_data, exp_value)
        resp = requests.post(user_url, data=user_data)

        # 改变username

    def test_case02(self):
        user_url = HOST + "/user"
        # 期望值
        exp_value = {
            "username": "pop2",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        # 实际值
        user_data = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        self.assertDictEqual(exp_value, user_data)
        # resp = requests.post(user_url, data=user_data)
        # print(resp.status_code)
        # print(resp.content)

    def test_case03(self):
        user_url = HOST + "/user"
        # 期望值
        exp_value = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwertqq.com",
            "password": "123456"
        }
        # 实际值
        user_data = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        self.assertDictEqual(exp_value, user_data)
        # resp = requests.post(user_url, data=user_data)
        # print(resp.status_code)
        # print(resp.content)

    def test_004(self):
        user_url = HOST + "/user"
        # print(user_url)
        exp_value = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        user_data = {
            "username": "pop4",
            "tel": "15738460225",
            "email": "qwert@qq.com",
            "password": "123456"
        }
        self.assertDictEqual(exp_value, user_data)
        resp = requests.post(user_url, data=user_data)
        # print(resp.status_code)
        # print(resp.content)

    def test_005(self):
        user_url = HOST + "/user"

        exp_value = {
            "username": "pop6",
            "tel": "12345",
            "email": "qwert@qq.com",
            "password": "1521234"
        }

        user_data = {
            "username": "pop6",
            "tel": "12345",
            "email": "123123123",
            "password": "1521234"
        }
        self.assertDictEqual(exp_value, user_data)
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)

    def test_case006(self):
        user_url = HOST + "/user"

        exp_value = {
            "username": "ty1",
            "tel": "15738460225",
            "email": "157@qq.com",
            "password": "123456"
        }

        user_data = {
            "username": "ty1",
            "tel": "15738460225",
            "email": "157@qq.com",
            "password": "123456"
        }

        self.assertDictEqual(exp_value, user_data)


    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
