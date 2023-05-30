# json.load将json文件转换为字典或者列表，但是json.load()方法只能处理单个 JSON 对象。
import json
with open("users.json", encoding="utf-8") as file:
    print(type("users.json"))
    two_dict = json.load(file)
    print(type(two_dict))
    print(two_dict)

    pass