import unittest
from ddt import ddt, file_data

from utils.UserUtils import UserAPI


@ddt
class TestAddUserTestCases(unittest.TestCase):

    @file_data("test_create_user.json")
    def test_add_user(self, username, password, email, tel, status_code, exp_str):
        resp = UserAPI.add_user(username, tel, email, password)

        exp_status = status_code
        act_status = resp[UserAPI.STATUS_CODE]
        self.assertEqual(exp_status, act_status)

        exp_content = exp_str
        act_content = UserAPI.get_all_users_list()
        self.assertDictContainsSubset(exp_content, act_content)


if __name__ == '__main__':
    unittest.main()
