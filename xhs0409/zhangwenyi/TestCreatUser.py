import unittest
import requests
from xhs0409.zhangwenyi.config import HOST
class MyTestCase(unittest.TestCase):
    def test_CU1(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop68",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 200
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册失败')
        print(resp.content)

    def test_CU2(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "zhangqiang1",
            "tel": "15237654877",
            "password": "12345678",
            "email": "1038764578"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 300
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)
        # print(type(Actual))
        # print(type(Except))

    def test_CU3(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop5",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        Except = 200
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

    def test_CU4(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "p@op3",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        resp = requests.post(user_url, data=user_data)
        Except = 400
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

    def test_CU5(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "aini1314",
            "tel": "1887777",
            "password": "aa12345",
            "email": "123@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 300
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

    def test_CU6(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "123",
            "tel": "15237930295",
            "password": "12345",
            "email": "2390084498@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 300
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

    def test_CU7(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "TY",
            "tel": "15738460225",
            "password": "Meng&cheng123",
            "email": "157@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 200
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

    def test_CU8(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "test005",
            "tel": "",
            "password": "mimabu123",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        Except = 200
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)
    def test_CU9(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "Qaq",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq"
        }
        resp = requests.post(user_url, data=user_data)
        Except = 200
        Actual = resp.status_code
        self.assertEqual(Except, Actual, msg='注册不成功')
        print(resp.content)

if __name__ == '__main__':
    unittest.main()






































































if __name__ == '__main__':
    unittest.main()
