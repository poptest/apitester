import unittest
import requests
from xhs0409.XuZhiFei.util.config import host
class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = host+"/user"
        status_code = 200
        resp = requests.get(url)
        print(resp.status_code)
        self.assertEqual(status_code, resp.status_code)
if __name__ == '__main__':
    unittest.main()
