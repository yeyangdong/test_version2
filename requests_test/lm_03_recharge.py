# 1.导入request库
import requests

# 2.登陆
login_url = "http://api.lemonban.com:8788/futureloan/member/login"

headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    "Content-Type": "application/json"
}

login_params = {
    "mobile_phone": "15158787682",
    "pwd": "12345678"
}
res_login = requests.post(url=login_url, json=login_params, headers=headers_dict)

response_data_dict = res_login.json()
token = response_data_dict["data"]["token_info"]["token"]
user_id =response_data_dict["data"]["id"]

# 3.注册
recharge_url = "http://api.lemonban.com:8788/futureloan/member/recharge"
recharge_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

recharge_params = {
    "amount": "10000",
    "member_id": user_id
}

recharge_res = requests.post(url=recharge_url, json=recharge_params, headers=recharge_dict)
pass