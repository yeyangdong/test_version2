
#0.导入yaml模块
import yaml

# 1.打开yaml配置文件
with open("testcase.yaml", encoding="utf-8") as file:
    # full_load方法加载
    data = yaml.full_load(file)
    pass