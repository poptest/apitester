import unittest
import requests
from xhs0409.XuZhiFei.util.config import host
from xhs0409.XuZhiFei.user.create_user_util import createUserUtil
class MyTestCase(unittest.TestCase):
    #正常创建用户
    def test_createUser001(self):
        stu_code = createUserUtil().createUserUtil("admin","123456","15936621234","107010@qq.com")
        self.assertEqual(200, stu_code,"创建用户出现异常")

    #测试账号重复
    def test_createUser002(self):
        stu_code = createUserUtil().createUserUtil("asdfasd","2312123","15936625167","107010@qq.com")
        if stu_code==300:
            self.assertEqual(300, stu_code, "测试账号不能重复,失败")
            return
        if stu_code==200:
            stu_code2 = createUserUtil().createUserUtil("asdfasd", "2312123", "15936625167", "107010@qq.com")
            self.assertEqual(300,stu_code2,"测试账号不能重复，失败")

    #测试邮箱格式
    def test_createUser003(self):
        stu_code = createUserUtil().createUserUtil("zhangqiang","2312123","15936622233","1038764578")
        self.assertNotEqual(200,stu_code,"测试邮箱格式，失败")

    # 测试邮箱为空
    def test_createUser004(self):
        stu_code = createUserUtil().createUserUtil("zhangqiang", "2312123", "15936622234","")
        self.assertNotEqual(200, stu_code, "测试邮箱格式，失败")

    # 测试账号含有特殊字符
    def test_createUser005(self):
        stu_code = createUserUtil().createUserUtil("zhang@qiang", "2312123", "15936622235", "1038764578@qq.com")
        self.assertEqual(200, stu_code, "测试账号含有特殊字符，失败")

    # 测试手机号码为7位(BUG：2019年04月09日15:14:47)
    def test_createUser005(self):
        stu_code = createUserUtil().createUserUtil("zhang@qiang", "2312123", "1593662", "1038764578@qq.com")
        self.assertNotEqual(200, stu_code, "测试手机号码为7位，出现异常")

if __name__ == '__main__':
    unittest.main()
