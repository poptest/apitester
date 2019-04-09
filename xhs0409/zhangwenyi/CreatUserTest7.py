import unittest
import requests
from config import HOST


class MyTestCase(unittest.TestCase):
    def test_CU7(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "TY",
            "tel": "15738460225",
            "password": "Meng&cheng123",
            "email": "157@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#password含有特殊字符，用户也能创建成功