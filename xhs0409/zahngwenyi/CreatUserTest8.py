import unittest
import requests
from config import HOST


class MyTestCase(unittest.TestCase):
    def test_CU8(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "test005",
            "tel": "",
            "password": "mimabu123",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#bug3tel和email均为空，也能注册成功