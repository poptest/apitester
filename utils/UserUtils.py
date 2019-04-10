import requests
import json
from config import HOST


def get_all_users_list():
    url = HOST + '/user'
    resp = requests.get(url)
    users_list_str = resp.content.decode('utf-8')
    users_dic = json.loads(users_list_str)
    users_list = users_dic['users']
    return users_list


def if_user_exist_by_username(username):
    users_list = get_all_users_list()
    for user in users_list:
        if user['username'] == username:
            return True
    return False
