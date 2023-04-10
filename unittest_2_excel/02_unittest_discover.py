import unittest




#1.使用unittest.defaultTestLoader.discover（）方法，返回套件对象
#a、第一个参数为发现用例的路径
#b、第二个参数为用例模块的匹配模式（test*.py）
suite = unittest.defaultTestLoader.discover(".")

#2.执行用例
#创建TextTestRunner()运行器
runner = unittest.TextTestRunner()

#3.运行套件里面的用例
runner.run(suite)