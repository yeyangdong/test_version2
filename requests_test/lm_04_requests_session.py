import requests

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
# 1.创建会话对象，相当于浏览器，会自动维护cookies信息
session = requests.session()

# 2.使用会话对象去发起请求
one_response = session.post(url=url, headers=header_dict, json=requests_params)

# 3.关闭会话,仅仅只是将资源释放，还是可以继续请求的
session.close()
pass
