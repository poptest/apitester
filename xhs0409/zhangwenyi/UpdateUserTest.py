import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):
    def test_UpdateUserTest(self):
        user_url = HOST+'/user'
        user_data = {
            "username": "zhangqi",
            "password": "123456",
            "tel": "13946342567",
            "email": "126366@qq.com"
        }
        resp = requests.put(user_url, json=user_data)
        print(resp.raw)
        print(resp.cookies)
        print(resp.headers)
        print(resp.content)

if __name__ == '__main__':
    unittest.main()
