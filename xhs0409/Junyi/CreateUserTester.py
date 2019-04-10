import unittest
import requests

from config import HOST


class MyTestCase(unittest.TestCase):

    def test_createuser_01(self):
        user_url = HOST + "/user"
        user_data = {
            "username": "pop2",
            "tel": "19908080808",
            "email": "wrwer@qq.com",
            "password": "141434234"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
