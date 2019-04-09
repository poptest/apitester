import unittest
import requests
from config import HOST
class MyTestCase(unittest.TestCase):
    def test_GetUserTest(self):
        url=HOST+'/user'
        resp=requests.get(url)
        print(resp)
        print(resp.url)
        print(resp.content.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
