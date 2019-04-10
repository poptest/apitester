import unittest
import requests
from xhs0409.TianYang.config import HOST

class Getcommunity(unittest.TestCase):

    def test_case01(self):

        url = HOST + "community"
        resp = requests.get(url)
        print(resp)
        print(resp.url)
        print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()