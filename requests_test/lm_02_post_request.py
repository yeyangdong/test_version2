# 1.导入request库
import requests

# 2.构造函数
url = "http://api.lemonban.com:8788/futureloan/member/register"

header_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    "Content-Type": "application/json"
}

requests_params = {
    "mobile_phone": "15158787682",
    "pwd": "12345678",
    "reg_name": "",
    "type": 0
}

res = requests.post(url=url, json=requests_params, headers=header_dict)
pass
