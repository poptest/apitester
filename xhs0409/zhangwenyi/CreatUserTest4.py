import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):
    def test_CU4(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "p@op3",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
