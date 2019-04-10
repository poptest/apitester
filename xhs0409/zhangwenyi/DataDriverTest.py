import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data('UserData.json')
    def test_data_from_json_file(self,username,email,tel,password):
        msg='User<%s>,email%s,tel%s,password%s'%(username,email,tel,password)
        print(msg)

    # @data(1, 2, 3)
    # def test_case001(self, value):
    #     a=value
    #     print(a)

    # @data({"name":"tom", "email":"tom@qq.com"},
    #       {"name":"Ann", "email":"Ann@qq.com"},
    #       {"name":"Lee", "email":"Lee@qq.com"})
    # def test_case001(self, value):
    #     a = value
    #     print(type(a))
    #     print(a)
    #     print(a['name'])

    # @data({"name": "tom", "email": "tom@qq.com"},
    #       {"name": "Ann", "email": "Ann@qq.com"},
    #       {"name": "Lee", "email": "Lee@qq.com"})
    # @unpack
    # def test_case001(self, name, email):
    #     print(name)
    #     print(email)




if __name__ == '__main__':
    unittest.main()
