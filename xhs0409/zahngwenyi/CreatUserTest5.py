import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):
    def test_CU5(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "aini1314",
            "tel": "1887777",
            "password": "aa12345",
            "email": "123@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#bug2七位手机号，还是注册成功
