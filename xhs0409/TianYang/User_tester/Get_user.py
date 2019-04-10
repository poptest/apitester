
import unittest
import requests

class Getuser(unittest.TestCase):

    def test_case01(self):
        url = "http://192.168.2.118:5000/user"
        resp = requests.get(url)
        print(resp)
        print(resp.url)
        print(resp.content.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()