import requests
import unittest
from config import HOST



class user_create(unittest.TestCase):
    def test_create01(self):
        # 手机号10位
        user_url = HOST + "/user"
        user_data = {
        	"username": "chai01",
            "password": "123456789",
            "tel": "1892222333",
            "email": "chai001@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        Expected =400
        Actual=resp.status_code
        self.assertEqual(Expected,Actual,msg='注册失败')
        print(resp.content)

    def test_create02(self):
        # 手机号12位
        user_url = HOST + "/user"
        user_data = {
        	"username": "chai002",
            "password": "123456789",
            "tel": "189222333331",
            "email": "chai001@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        #期望值：Expected
        Expected =400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual=resp.status_code
        self.assertEqual(Expected,Actual,msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create03(self):
        # 邮箱格式无@
        user_url = HOST + "/user"
        user_data = {
            "username": "chai003",
            "password": "123456789",
            "tel": "18922233333",
            "email": "chai001qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)
    def test_create04(self):
        # 注册用户正常
        user_url = HOST + "/user"
        user_data = {
            "username": "chai004",
            "password": "123456789",
            "tel": "18922233333",
            "email": "chai001@qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 200
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create05(self):
        # 邮箱为纯数字
        user_url = HOST + "/user"
        user_data = {
            "username": "chai005",
            "password": "123456789",
            "tel": "18922233333",
            "email": "chai001qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create06(self):
        # 邮箱为空
        user_url = HOST + "/user"
        user_data = {
            "username": "chai006",
            "password": "123456789",
            "tel": "18922233333",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create07(self):
        # 用户名含有特殊符号
        user_url = HOST + "/user"
        user_data = {
            "username": "@chai007",
            "password": "123456789",
            "tel": "18922233333",
            "email": "chai001qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create08(self):
        # 用户名为纯数字
        user_url = HOST + "/user"
        user_data = {
            "username": "008",
            "password": "123456789",
            "tel": "18922233333",
            "email": "chai001qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create09(self):
        # 密码含有特殊字符
        user_url = HOST + "/user"
        user_data = {
            "username": "chai09",
            "password": "@123456789",
            "tel": "18922233333",
            "email": "chai001qq.com"
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

    def test_create10(self):
        # 手机号、邮箱为空
        user_url = HOST + "/user"
        user_data = {
            "username": "chai010",
            "password": "123456789",
            "tel": "",
            "email": ""
        }
        resp = requests.post(user_url, data=user_data)
        # 期望值：Expected
        Expected = 400
        # Actual：实际值；返回状态码 （.status_code） 例：200
        Actual = resp.status_code
        self.assertEqual(Expected, Actual, msg='注册失败')
        # 打印内容（.content）
        print(resp.content)

if __name__ == '__main__':
    unittest.main()