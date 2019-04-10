import unittest
from xhs0409.XuZhiFei.user.create_user_util import createUserUtil
from xhs0409.XuZhiFei.util import UserUtils
import random
class MyTestCase(unittest.TestCase):
    #正常创建用户
    def test_createUser001(self):
        username = "admin"       #账号
        password = "123456"      #密码
        tel = "15936621234"      #手机号
        email ="107010@qq.com"   #电子邮箱
        stu_username = UserUtils.if_user_exist_by_username(username) #判断账号是存在
        if stu_username == True :
            print("test_createUser001因为账号存在无法正常此用例")
            return
        stu_tel = UserUtils.if_user_exist_by_tel(tel)               #判断手机号是否存在
        if stu_tel == True :
            print("test_createUser001因为手机号存在无法正常此用例")
            return
        stu_code = createUserUtil().createUserUtil(username,password, tel,email) #创建用户
        self.assertEqual(200, stu_code, "创建用户出现异常")


    #测试账号重复
    def test_createUser002(self):
        username = "admin"  # 账号
        password = "123456"  # 密码
        tel = "15936621234"  # 手机号
        email = "107010@qq.com"  # 电子邮箱
        stu_tel = UserUtils.if_user_exist_by_tel(tel)  # 判断手机号是否存在
        if stu_tel == True:
            print("test_createUser001因为手机号存在无法正常此用例")
            return
        stu_username = UserUtils.if_user_exist_by_username(username) #判断账号是否存在
        if stu_username == True:
            stu_code = createUserUtil().createUserUtil(username,password, tel,email)
            self.assertEqual(300, stu_code2, "测试账号不能重复，失败")
        else:
            createUserUtil().createUserUtil(username, password, tel, email)
            stu_code = createUserUtil().createUserUtil(username, password,int(tel)+1, email)
            self.assertEqual(300,stu_code,"测试账号不能重复，失败")


    #测试邮箱格式
    def test_createUser003(self):
        stu_code = createUserUtil().createUserUtil("asd1","2312123","15936622233","1038764578")
        print(stu_code)
        self.assertNotEqual(200,stu_code,"测试邮箱格式，失败")

    # 测试邮箱为空
    def test_createUser004(self):
        stu_code = createUserUtil().createUserUtil("asd3", "2312123", "15936622234","")
        print(stu_code)
        self.assertNotEqual(200, stu_code, "测试邮箱为空，失败")

    # 测试账号含有特殊字符
    def test_createUser005(self):
        stu_code = createUserUtil().createUserUtil("zhang@qiang", "2312123", "15936622235", "1038764578@qq.com")
        self.assertEqual(200, stu_code, "测试账号含有特殊字符，失败")

    # 测试手机号码为7位(BUG：2019年04月09日15:14:47)
    def test_createUser006(self):
        stu_code = createUserUtil().createUserUtil("zhang@asd", "2312123", "1593662", "1038764578@qq.com")
        self.assertNotEqual(200, stu_code, "测试手机号码为7位，出现异常")

    # 测试账号为空
    def test_createUser007(self):
        stu_code = createUserUtil().createUserUtil("", "2312123", "15936625167", "1038764578@qq.com")
        self.assertNotEqual(200, stu_code, "测试账号为空，出现异常")

    # 测试密码可以含有中文
    def test_createUser008(self):
        stu_code = createUserUtil().createUserUtil("asdw", "瓦达瓦大", "15936625167", "1038764578@qq.com")
        self.assertNotEqual(200, stu_code, "测试账号为空，出现异常")
if __name__ == '__main__':
    unittest.main()
