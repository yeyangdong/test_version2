# 1.导入request库
import requests

# 2.构造函数
url = "http://api.lemonban.com:8788/futureloan"

header_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky"
}

params_dict = {
    "pageIndex": 2,
    "pageSize": 2
}

res = requests.get(url, headers=header_dict, params=params_dict)
pass
