import unittest
import requests
from config import HOST

class user_put(unittest.TestCase):
    def test_something(self):
        # 更新用户信息
        user_url = HOST + "user"
        user_data = {
            "username": "chai",
            "password": "2123456789",
            "tel": "18922223333",
            "email": "chai@qq.com"
        }
        resp = requests.put(user_url, json=user_data)
        print(resp.raw)
        print(resp.cookies)
        print(resp.headers)
        print(resp.content)
        print(resp.status_code)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
