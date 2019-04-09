import unittest
import requests
from config import HOST
class MyTestCase(unittest.TestCase):
    def test_CreatUser(self):
        user_url = HOST+'/user'
        user_data={
            "username":"zhangguoliang",
            "password":"123456",
            "tel":"13946342567",
            "email":"126366@qq.com"
        }
        resp=requests.post(user_url,data=user_data)
        print(resp.status_code)
        print(resp.content)
    def test_CU1(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop3",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": "qsong.vip@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)
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
        # bug1邮箱格式不正确，也能成功注册一个用户
    def test_CU3(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop3",
            "tel": "19907131352",
            "password": "Aa12345678",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        print(resp.content)
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
