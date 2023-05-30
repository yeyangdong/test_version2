# json.dumps将字典,列表转换为字符串

import json

one_dict = {
    "name": "叶洋东三号",
    "age": "18",
    "hobby": ["玩游戏", "读书"]
}
print(type(one_dict))
json_str = json.dumps(one_dict, ensure_ascii=False) #默认情况dumps会将中文转换为ascii码，这边设置fasle就可以展示中文
print(type(json_str))
