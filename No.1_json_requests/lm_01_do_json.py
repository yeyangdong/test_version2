import requests
import json
# json.loads将json字符串转换为字典或者数组
one_str = '{"name" : "叶洋东一号", "age":"18"}'
one_dict = json.loads(one_str)
print(type(one_str))
print(one_dict)
print(type(one_dict))




