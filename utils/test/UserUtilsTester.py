import unittest
from utils import UserUtils


class MyUserUtilsTester(unittest.TestCase):


    def test_get_all_users_list(self):
        users_list = UserUtils.get_all_users_list()
        print(users_list)

    def test_if_user_exist_by_username_false(self):
        exp_value = False
        username = "wejoweow"
        act_value = UserUtils.if_user_exist_by_username(username)

        self.assertEqual(exp_value, act_value)

    def test_if_user_exist_by_username_true(self):
        exp_value = True
        username = "admin"
        act_value = UserUtils.if_user_exist_by_username(username)

        self.assertEqual(exp_value, act_value)



if __name__ == '__main__':
    unittest.main()
