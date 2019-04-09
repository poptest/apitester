import unittest
import requests
from config import HOST


class MyTestCase(unittest.TestCase):
    def test_CU6(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "123",
            "tel": "15237930295",
            "password": "12345",
            "email": "2390084498@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#username为纯数字，也能注册成功
