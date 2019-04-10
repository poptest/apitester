import unittest
from ddt import ddt, data, unpack, file_data

@ddt
class TestMyCase(unittest.TestCase):

    @file_data("UserData.json")
    def test_data_from_json_file(self, username, email, tel, password):
        msg = "User<%s>, email->%s, tel->%s, password->%s" % (username, email, tel, password)
        print(msg)

    @data(1, 2, 3, 4)
    def test_01(self, value):
        print(value)
        self.assertEqual(True, False)

    @data({"username":"tom", "email":"tom@qq.com"},
          {"username":"XiaoMing", "email":"xiaoming@qq.com"})
    def test_data(self, value):
        print(value['username'])
        print(value['email'])

    @data({"username": "tom", "email": "tom@qq.com", "tel":"111", "password":"adafs"},
          {"username": "tom", "email": "tom", "tel":"111", "password":"adafs"})
    @unpack
    def test_unpack(self, username, email, tel, password):
        print(username)
        print(email)
        print(tel)
        print(password)


if __name__ == '__main__':
    unittest.main()
