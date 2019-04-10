import requests
import json

from config import CREATE_USER_URL


class UserAPI(object):

    STATUS_CODE = 'status_code'
    CONTENT = 'content'

    @classmethod
    def add_user(cls, username, password, email, tel):
        __user_data = {
            'username': username,
            'password': password,
            'email': email,
            'tel': tel
        }
        __resp = requests.post(CREATE_USER_URL, data=__user_data)
        __ret_val = {
            'status_code': str(__resp.status_code),
            'content': __resp.content
        }
        return __ret_val


    @classmethod
    def get_all_users_list(cls):
        resp = requests.get(CREATE_USER_URL)
        users_list_str = resp.content.decode('utf-8')
        users_dic = json.loads(users_list_str)
        users_list = users_dic['users']
        return users_list

    @classmethod
    def if_user_exist_by_username(cls, username):
        users_list = cls.get_all_users_list()
        for user in users_list:
            if user['username'] == username:
                return True
        return False
