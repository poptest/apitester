import unittest
import requests
from config import HOST

class MyTestCase(unittest.TestCase):
    def test_normal(self):
        user_url = HOST+"/user"
        user_date = {
             "username": "test003",
             "password": "12345678990",
             "tel": "12345678901",
             "email": "test@.com"
        }
        resp01 = requests.post(user_url,data=user_date)
        print(resp01.status_code)
        # print(resp.content)


    def test_wrongemail(self):
        user_url = HOST+"/user"
        user_date = {
             "username": "test003",
             "password": "12345678990",
             "tel": "12345678901",
             "email": "test"
        }
        resp02 = requests.post(user_url,data=user_date)
        print(resp02.status_code)
        # print(resp.content)

    def test_noemail(self):
        user_url = HOST+"/user"
        user_date = {
             "username": "test003",
             "password": "12345678990",
             "tel": "12345678901",
             "email": ""
        }
        resp03 = requests.post(user_url,data=user_date)
        print(resp03.status_code)
        print(resp03.content)

    def test_wrongUsername(self):
        user_url = HOST+"/user"
        user_date = {
            "username": "test@003",
            "password": "12345678990",
            "tel": "12345678901",
            "email": ""
        }
        resp04 = requests.post(user_url, data=user_date)
        print(resp04.status_code)
        # print(resp04.content)
    def test_7tel(self):
         user_url = HOST+"/user"
         user_date = {
             "username": "test003",
             "password": "1234567",
             "tel": "12345678901",
             "email": ""
         }
         resp05 = requests.post(user_url, data=user_date)
         print(resp05.status_code)
         print(resp05.content)

if __name__ == '__main__':
    unittest.main()