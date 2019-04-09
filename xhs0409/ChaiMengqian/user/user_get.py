import unittest
import requests
from config import HOST

class user_get(unittest.TestCase):

    def test_get01(self):
        #获取全部用户信息
        url = HOST + "user"
        resp01 = requests.get(url)
        print(resp01)
        print(resp01.url)
        print(resp01.content.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
