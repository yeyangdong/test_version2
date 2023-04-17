import json

from unitest_test.handle_request import HandleRequest

do_requset = HandleRequest()

# 1.构造请求参数
register_url = "http://api.lemonban.com:8788/futureloan/member/register"
header_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky",
    "Content-Type": "application/json"
}

do_requset.add_headers(header_dict)

requests_params = {
    "mobile_phone": "15158787682",
    "pwd": "12345678",
    "reg_name": "",
    "type": 0
}

# 2.发起请求
res = do_requset.send(method="post", url=register_url, json=requests_params)

# 3.提取相应数据，然后断言
expected_value = 0
real_code = res.json()["code"]

if expected_value == real_code:
    print("success")
else:
    print("false")

