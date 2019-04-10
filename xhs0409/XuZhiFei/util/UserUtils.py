import requests
import json

from xhs0409.XuZhiFei.util.config import host

def get_all_users_list():
    url = host + '/user'
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
#查询手机号是否存在
def if_user_exist_by_tel(tel):
    users_list = get_all_users_list()
    for user in users_list:
        if user['tel'] == tel:
            return True

    return False