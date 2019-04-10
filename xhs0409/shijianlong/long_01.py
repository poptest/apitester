# -*- coding:utf-8 -*-

import unittest
import requests
from config import HOST
from utils import UserUtils


class UserTestCase(unittest.TestCase):
        # 正常创建
    def test_createUser_01(self):
        user_url = HOST + '/user'
        # 定义一个字典
        user_date = {
            "username": "pop120",
            "tel": "15523456789",
            "email": "1234560@pp.com",
            "password": "123456"
        }
        resp = requests.post(user_url,data=user_date)
        print(resp.status_code)
        #预期值
        expected = 200
        # 实际获取返回的状态码
        actual=resp.status_code
        #断言
        self.assertEqual(expected,actual,msg='注册失败！')
        # UserUtils.if_user_exist_by_username('pop120')
        # 打印内容
        # print(resp.content.decode('utf8'))

        # 邮箱格式不正确
    def test_createUser_02(self):
        user_url = HOST + '/user'
        user_date = {
            "username": "pop221",
            "tel": "15523456789",
            "email": "1234560",
            "password": "123456"
        }
        resp = requests.post(user_url,data=user_date)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected,actual,msg='出现BUG，邮箱格式不正确！')

        # 邮箱输入为空
    def test_createUser_03(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop331",
            "tel": "15511110000",
            "email": "",
            "password": "123456"
        }
        resp = requests.post(user_url,data=user_data)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected,actual,msg='出现BUG，邮箱不能为空！')

        # 手机号为7位
    def test_createUser_04(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop332",
            "tel": "1551111",
            "email": "",
            "password": "123456"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected, actual, msg='出现BUG，手机号长度为11位！')

        #password含有特殊字符
    def test_createUser_05(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop333",
            "tel": "15511110000",
            "email": "123e@qq.com",
            "password": "123、456"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected, actual, msg='出现BUG，密码不能含有特殊字符！')

        # 手机号为空
    def test_createUser_06(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "pop334",
            "tel": "",
            "email": "123e@qq.com",
            "password": "123、456"
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected, actual, msg='出现BUG，手机号不能为空！')

        # 密码为空
    def test_createUser_07(self):
        user_url = HOST + '/user'
        user_data = {
            "username": "POP123",
            "tel": "14711110000",
            "email": "12113e@qq.com",
            "password": ""
        }
        resp = requests.post(user_url, data=user_data)
        print(resp.status_code)
        expected = 400
        actual = resp.status_code
        self.assertEqual(expected, actual, msg='出现BUG，密码不能为空！')


if __name__ == '__main__':
    unittest.main()
