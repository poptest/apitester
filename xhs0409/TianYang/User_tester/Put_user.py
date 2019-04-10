import unittest
import requests

class Putuser(unittest.TestCase):

    def test_case04(self):
        user_url = "http://192.168.2.118:5000/user"
        user_data = {
            "username": "pop9",
            "tel": "12345",
            "email": "qwert@qq.com",
            "password": "15212345678"
        }
        resp = requests.post(user_url, json=user_data)
        print(resp.raw)
        print(resp.cookies)
        print(resp.headers)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()