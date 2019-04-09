import unittest
import requests
from xhs0409.XuZhiFei.util.config import host
class MyTestCase(unittest.TestCase):
    def test_updateUser(self):
        status_code = 200
        user_url = host+"/user"
        user_data={
            "username": "admin2",
            "password": "admin",
            "tel": "19907131351",
            "email": "qsong.vip@qq.com"
        }
        resp = requests.put(user_url, json=user_data)
        self.assertEqual(status_code, resp.status_code,"创建用户出现异常")


if __name__ == '__main__':
    unittest.main()
