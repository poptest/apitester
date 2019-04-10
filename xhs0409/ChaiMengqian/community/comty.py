import unittest
import requests
from xhs0409.ChaiMengqian.config import HOST

class community(unittest.TestCase):

    def test_comty01(self):
        # 获取社区列表
        url = HOST + "/community"
        resp = requests.get(url)
        print(resp)
        print(resp.url)
        print(resp.content.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
