import unittest
from utils import UserUtils


class MyUserUtilsTester(unittest.TestCase):


    def test_get_all_users_list(self):
        users_list = UserUtils.get_all_users_list()
        print(users_list)



if __name__ == '__main__':
    unittest.main()
