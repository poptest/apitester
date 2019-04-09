import unittest
import requests
from config import HOST


class MyTestCase(unittest.TestCase):
    def test_createuser_01(self):
        self.user_url = HOST + '/user'
        # 定义一个字典
        user_date = {
            "username": "pop11",
            "tel": "15523456789",
            "email": "1234560@pp.com",
            "password": "123456"
        }
        resp = requests.post(self.user_url,data=user_date)
        print(resp.status_code)
        expected = 200
        # 获取返回的状态码
        actual=resp.status_code
        self.assertEqual(expected,actual,msg='注册失败！')
        # 打印内容
        print(resp.content.decode('utf8'))

    def test_createuser_02(self):
        # 邮箱格式不正确
        user_date = {
            "username": "pop22",
            "tel": "15523456789",
            "email": "1234560",
            "password": "123456"
        }
        resp = requests.post(self.user_url,data=user_date)
        print(resp.status_code)
        expected = 200
        actual = resp.status_code
        self.assertEqual(expected,actual,msg='注册失败，邮箱格式不正确！')

    def test_createuser_03(self):
        user_data = {
            "username": "pop33",
            "tel": "15511110000",
            "email": "",
            "password": "123456"
        }
        resp = requests.post(self.user_url,data=user_data)
        print(resp.status_code)
        expected = 200
        actual = resp.status_code
        self.assertEqual(expected,actual,msg='注册失败，邮箱不能为空！')


if __name__ == '__main__':
    unittest.main()
