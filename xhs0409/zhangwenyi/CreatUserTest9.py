import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):
    def test_CU9(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "Qaq",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#bug4邮箱后缀没有.com，也能注册成功
