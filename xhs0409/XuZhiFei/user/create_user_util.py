from xhs0409.XuZhiFei.util.config import host
import requests
class createUserUtil():
    def createUserUtil(self,username,password,tel,email):
        user_url = host+"/user" #请求地址
        user_data={
            "username": username,
            "password": password,
            "tel": tel,
            "email": email
        }
        get_resp = requests.get(user_url)
        resp = requests.post(user_url, data=user_data)
        return resp.status_code