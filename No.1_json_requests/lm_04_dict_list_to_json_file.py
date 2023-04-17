# json.dump将字典，列表写成json文件

import json

one_dict = {
    "name": "叶洋东三号",
    "age": "18",
    "hobby": ["玩游戏", "读书"]
}

with open("users_write.json", "w", encoding="utf-8") as file:
    json.dump(one_dict, file, ensure_ascii=False, indent=2)
    pass
