import unittest
from ddt import ddt,data,unpack,file_data


@ddt
class MyTestCase(unittest.TestCase):

    @file_data("UserData.json")
    def test_001(self,username,email,tel,password):
        msg="user:%s, email:%s, tel:%s, password:%s" % (username,email,tel,password)
        print(msg)

    # @data(1,2,3,4)
    # def test_01(self,value):
    #     print(value)
    #     self.assertEqual(True, False)

    # @data({"username":"tom","email":"1232@qq.com"},
    #       {"username":"joy","email":"321@qq.com"})
    # def test_02(self,value):
    #     print(type(value))
    #     print(value["username"])
    #     print(value["email"])
    # #
    # @data({"username":"tom","email":"1232@qq.com","password":"tom123","tel":"155"},
    #       {"username":"joy","email":"321@qq.com","password":"joy123","tel":"166"})
    #
    # @unpack
    # def test_Unpack(self,username,email,tel,password):
    #     print(username)
    #     print(email)
    #     print(tel)
    #     print(password)


if __name__ == '__main__':
    unittest.main()
