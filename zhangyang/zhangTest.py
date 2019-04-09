from config import HOST
import requests

user_url=HOST+"/user"
resp = requests.post(user_url)
print(resp.status_code)
print(resp.content)



# a=1
# b=2
# assert(a<b)
