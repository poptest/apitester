import unittest
import requests
from config import HOST


class MyTestCase(unittest.TestCase):
    def test_CU2(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "zhangqiang1",
            "tel": "15237654877",
            "password": "12345678",
            "email": "1038764578"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)


if __name__ == '__main__':
    unittest.main()
#bug1邮箱格式不正确，也能成功注册一个用户